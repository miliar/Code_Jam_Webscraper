#include<iostream>
#include<fstream>
#include <cstring>
#include <cmath>
#include <cstdlib>
using namespace std;

int a[10][10];
bool judge()
{
    int A,B;
    cin>>A>>B;
    short flag1=1,flag2=1;
    for (int i=0; i<A; i++) {
        for (int j=0; j<B; j++) {
            cin>>a[i][j];
        }
    }
    for (int i=0; i<A; i++)
    {
        for (int j=0; j<B; j++)
        {
            flag1=1;
            flag2=1;
            if (a[i][j]==1) {
                for (int m=0; m<B; m++) {
                    if (a[i][m]==2) {
                        flag1=0;
                        break;
                    }
                    
                }
                for (int m=0; m<A; m++) {
                    if (a[m][j]==2) {
                        flag2=0;
                        break;
                    }
                }
            }
            if ((flag1|flag2)==0) {
                return false;
            }
        }
    }
    return true;


}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int T;
	cin >> T;
	for (int k=1;k<=T;k++)
	{

        if (judge()==true) {
            cout<<"Case #"<<k<<": YES"<<endl;
        }
        else cout<<"Case #"<<k<<": NO"<<endl;
    }
	return 0;
}