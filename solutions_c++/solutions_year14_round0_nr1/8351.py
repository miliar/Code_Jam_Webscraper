#include <iostream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <bitset>
#include <cstring>
#include <vector>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin >> T;
    for(int t=0;t<T;t++)
    {
        int n1,n2,arr1[16],arr2[16],out,counter=0;
        cin >> n1;
        for(int i=0;i<16;i++){
            cin >> arr1[i];
        }
        cin >> n2;
        for(int i=0;i<16;i++)
            cin >>arr2[i];
        int might[4];
        for(int k=(n1-1)*4;k< n1*4;k++)
        {
            might[k%4]=arr1[k];
        }
        for(int k=(n2-1)*4;k< n2*4;k++)
        {
            for(int i=0;i<4;i++){
                if(arr2[k]==might[i]){
                    if(counter==0)
                        out=might[i];
                    counter++;
                }
            }
        }
        printf("Case #%d: ",t+1);
        if(counter==1)
            cout << out << endl;
        else if(counter>1)
            cout << "Bad magician!\n";
            else
                cout << "Volunteer cheated!\n";
    }
}
