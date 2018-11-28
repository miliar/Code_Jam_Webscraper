#include <fstream>
#include <string>
#include <sstream>
#include <iomanip>
using namespace std;

#define swap(type, a, b) {type temp = a; a = b; b = temp; } // hang hoan vi
 
void quickSort(double a[], int l, int r)
{
    srand(time(NULL));  //khoi tao tham so ham rand()
    double key = a[l + rand() % (r-l+1)];  //lay khoa la gia tri ngau nhien tu a[l] -> a[r]
    //int key = a[(l+r)/2];
    int i = l, j = r;
 
    while(i <= j)
    {
        while(a[i] < key) i++;       // tim phan tu ben trai ma >=key
        while(a[j] > key) j--;       // tim phan tu ben trai ma <=key
        if(i <= j)
        {
            if (i < j)
                swap(double, a[i], a[j]);  // doi cho 2 phan tu kieu int a[i], a[j].
            i++;
            j--;
        }
    }
    //bay gio ta co 1 mang : a[l]....a[j]..a[i]...a[r]
    if (l < j) quickSort(a, l, j);   // lam lai voi mang a[l]....a[j]
    if (i < r) quickSort(a, i, r); // lam lai voi mang a[i]....a[r]
}

int main () {

    ifstream read("input.txt");
    ofstream myfile;
    myfile.open("output.txt");
    int t; // Number of test cases
    int n; // Number of stones
    int temp_index_top, temp_index_bottom;
    int naomi_index_top, naomi_index_bottom;
    int ken_index_top, ken_index_bottom;
    int rs_deceive = 0, rs_normal = 0;
    double naomi[1001], ken[1001];
    bool chosen_naomi[1001], chosen_ken[1001];
    read >> t;
    for (int z = 0; z < t; z++)
    {
        myfile << "Case #" << (z+1) << ": ";
        read >> n;
        for (int i = 0; i < n; i++)
            read >> naomi[i];
        for (int i = 0; i < n; i++)
            read >> ken[i];
        quickSort(naomi, 0, n-1);
        quickSort(ken, 0, n-1); 
        
        // Calculating rs_normal       
        for (int i = 0; i < n; i++)
        {
            chosen_naomi[i] = false;
            chosen_ken[i] = false;
        } 
        temp_index_top = n-1;
        temp_index_bottom = 0;
        rs_normal = 0;
        for (int i = n-1; i >= 0; i--)
        {
            if (ken[temp_index_top] > naomi[i])
            {
               chosen_naomi[i] = true;
               chosen_ken[temp_index_top] = true;
               temp_index_top = temp_index_top - 1;
            }
            else
            {
               rs_normal = rs_normal + 1;
               chosen_naomi[i] = true;
               chosen_ken[temp_index_bottom] = true;
               temp_index_bottom ++;
            }
        }
        
        // Calculating rs_deceive
        for (int i = 0; i < n; i++)
        {
            chosen_naomi[i] = false;
            chosen_ken[i] = false;
        }         
        rs_deceive = 0;
        for (int nbOfDeceiving = 0; nbOfDeceiving < n; nbOfDeceiving ++) 
        {
            int temp_rs_deceive = 0;
            naomi_index_top = n-1;
            naomi_index_bottom = 0;
            ken_index_top = n-1;
            ken_index_bottom = 0;
            for (int i = 0; i < n; i++) // n rounds
            {
                if (i < nbOfDeceiving)
                {
                   if (naomi[naomi_index_bottom] < ken[ken_index_top])
                   {
                      ken_index_top = ken_index_top - 1;
                      naomi_index_bottom ++;
                   }  
                   else
                   {
                      temp_rs_deceive = naomi_index_top - naomi_index_bottom + 1;
                      break;
                   }
                }
                else
                {
                   if (ken[ken_index_top] > naomi[naomi_index_top])
                   {
                      ken_index_top = ken_index_top - 1;
                      naomi_index_top = naomi_index_top - 1;           
                   }    
                   else
                   {
                      temp_rs_deceive ++;
                      ken_index_top = ken_index_top - 1;
                      naomi_index_top = naomi_index_top - 1;     
                   }
                }
            }
            if (temp_rs_deceive > rs_deceive)
               rs_deceive = temp_rs_deceive;
        }
        
        myfile << rs_deceive << " " << rs_normal << "\n";
        //
    }
    myfile.close();
}
