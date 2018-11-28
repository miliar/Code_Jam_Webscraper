#include <iostream>
#include <fstream>
using namespace std;
//#define ff cout
int input(int a[][4]);
int main()
{
   ofstream ff;
   ff.open("CJ1.txt");
    int t,n1,n2,a1[4][4],a2[4][4];
    int i,j,temp,c,flag;
    cin >> t;
    c = 1;
    while (t--) {
        flag = 0;
        n1 = input(a1);
        n1--;
        n2 = input(a2);
        n2--;
    for (i = 0; i < 4; i++){
        for (j = 0; j < 4; j++){
         // ff << "     " << a1[n1][i] << a2[n2][j] << endl;
            if(a1[n1][i] == a2[n2][j]) {
               flag++;
               temp = a1[n1][i];
            }
            if (flag == 2)
                break;
            }
        }
        if (flag == 1) {
           ff << "Case #" << c << ": " << temp << "\n";
        } else if (flag == 0)
            ff << "Case #" << c << ": Volunteer cheated!\n";
        else
            ff << "Case #" << c << ": Bad magician!\n";
    c++;
    }
ff.close();
    return 0;
}
 int input(int a[][4])
 {
    int n,i,j;
    cin >> n;
    for (i = 0; i < 4; i++)
        for (j = 0; j < 4; j++)
           cin >> a[i][j];
    return n;
 }
