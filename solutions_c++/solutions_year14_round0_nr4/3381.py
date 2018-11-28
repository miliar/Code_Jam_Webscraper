#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

void input(double a[] , double b[]);
void output(double a[]);
void initial(double a[],int t);
void merge_sort_asc(double a[],int low,int high);
void merge_asc(double a[],int l ,int m , int h);
void merge_sort_desc(double a[],int low,int high);
void merge_desc(double a[],int l ,int m , int h);
int war(double a[] , double b[]);
int deceit_war(double a[] , double b[]);
ifstream in("test1.txt",ios::in);
ofstream out("result2.txt",ios::out);

int n = 0;

int main()
{
    int i = 0 ,test_cases = 0,res1 = 0 ,res2 = 0;
    char c;
    double a[1000],b[1000];
    in.get(c);
    while(c != '\n')
    {
        test_cases = (test_cases * 10) + (int)c - 48;
        in.get(c);
    }
    for(i = 0 ; i < test_cases ; i++)
    {
        initial(a,1000);
        initial(b,1000);
        input(a,b);
//        output(a);
  //      output(b);
        res1 = war(a,b);
        res2 = deceit_war(a,b);
        cout<<"Case #"<<i+1<<": "<<res2<<" "<<res1<<"\n";
        output(a);
        cout<<"\n";
        output(b);
        cout<<"\n";
        out<<"Case #"<<i+1<<": "<<res2<<" "<<res1<<"\n";
        //cin>>c;
    }
    return 0;
}

void initial(double a[] , int t)
{
        int i = 0;
        for(i = 0 ;  i < t ; i++)
        {
            a[i] = 0.0;
        }
}

void input(double a[1000] , double b[1000])
{
    n = 0;
    int i = 0 ;
    in>>n;
    for(i = 0 ; i < n ;i++)
    {
        in>>std::fixed>>std::setprecision(9)>>a[i];
    }

    for(i = 0 ; i < n ;i++)
    {
        in>>std::fixed>>std::setprecision(9)>>b[i];
    }
}

void output(double a[1000])
{
    for(int i = 0 ; i < n ;i++)
    {
        cout<<std::fixed<<std::setprecision(9)<<a[i]<<" ";
    }
}


void merge_asc(double* input, int p, int r)
{
    int mid = ((p + r) / 2);
    int i1 = 0;
    int i2 = p;
    int i3 = mid + 1;

    // Temp array
    double temp[r-p+1];

    // Merge in sorted form the 2 arrays
    while ( i2 <= mid && i3 <= r )
        if ( input[i2] < input[i3] )
            temp[i1++] = input[i2++];
        else
            temp[i1++] = input[i3++];

    // Merge the remaining elements in left array
    while ( i2 <= mid )
        temp[i1++] = input[i2++];

    // Merge the remaining elements in right array
    while ( i3 <= r )
        temp[i1++] = input[i3++];

    // Move from temp array to master array
    for ( int i = p; i <= r; i++ )
        input[i] = temp[i-p];
}

void merge_sort_asc(double* input, int p, int r)
{
    if ( p < r )
    {
        int mid = ((p + r) / 2);
        merge_sort_asc(input, p, mid);
        merge_sort_asc(input, mid + 1, r);
        merge_asc(input, p, r);
    }
}


void merge_desc(double* input, int p, int r)
{
    int mid = ((p + r) / 2);
    int i1 = 0;
    int i2 = p;
    int i3 = mid + 1;

    // Temp array
    double temp[r-p+1];

    // Merge in sorted form the 2 arrays
    while ( i2 <= mid && i3 <= r )
        if ( input[i2] > input[i3] )
            temp[i1++] = input[i2++];
        else
            temp[i1++] = input[i3++];

    // Merge the remaining elements in left array
    while ( i2 <= mid )
        temp[i1++] = input[i2++];

    // Merge the remaining elements in right array
    while ( i3 <= r )
        temp[i1++] = input[i3++];

    // Move from temp array to master array
    for ( int i = p; i <= r; i++ )
        input[i] = temp[i-p];
}

void merge_sort_desc(double* input, int p, int r)
{
    if ( p < r )
    {
        int mid = ((p + r) / 2);
        merge_sort_desc(input, p, mid);
        merge_sort_desc(input, mid + 1, r);
        merge_desc(input, p, r);
    }
}

int war(double a[] , double b[])
{
    double c[1000],d[1000];
    int i = 0 , j = 0 , count = 0 , win_ken = 0 , k = 0;
    for(i = 0 ; i < n ; i++)
    {
        c[i] = a[i];
        d[i] = b[i];
    }
    merge_sort_asc(c,0,n-1);
    merge_sort_asc(d,0,n-1);

    for(i = 0 ; i < n ; i++)
    {
        for(j = 0 ; j < n ; j++ )
        {
            if(d[j] > c[i])
            {
                win_ken++;
                c[i] = 0.0;
                d[j] = 0.0;
                break;
            }
        }
    }
    return (n - win_ken);
}

int deceit_war(double a[], double b[])
{
    double c[1000],d[1000];
    int i = 0 , j = 0 , count = 0 , win_naomi = 0 , k = 0;
    for(i = 0 ; i < n ; i++)
    {
        c[i] = a[i];
        d[i] = b[i];
    }
    merge_sort_asc(c,0,n-1);
    /*cout<<"c\n";
    output(c);
    cout<<"\nd\n";
    output(d);
    cout<<"\n";*/
    merge_sort_desc(d,0,n-1);
    j = n - 1;
   for( i = 0 ; i < n ; i++)
   {


           if(d[i] < c[j])
           {
               win_naomi++;
               d[i] = 0.0;
               c[j] = 0.0;
               j--;

           }
           else
            {
                d[i] = 0.0;
                c[k] = 0.0;
                k++;

            }

   }
   return win_naomi;
}
