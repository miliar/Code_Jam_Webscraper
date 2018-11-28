#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include<math.h>
using namespace std;
void shift(char *b,int i){
    for(int j=i;j>=0;j--)
        b[j+1]=b[j];
}
int main()
{
    FILE *fin = freopen("A-large1.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("B11.out", "w", stdout);
    int t,n,j,h=1,temp;
    char a[1100],b[1100];
    cin>>t;
    for(int k=1;k<=t;k++){
        for(int i=0;i<1100;i++){
            a[i]='\0';
            b[i]='\0';
        }
        cin>>a;
        b[0]=a[0];
        for(int i=1;a[i];i++){
            if(a[i]>=b[0]){
                shift(b,i-1);
                b[0]=a[i];
            }
            else{
                b[i]=a[i];
            }
        }
        cout << "Case #"<< k << ": ";
        for(int i=0;b[i];i++)
            cout<<b[i];
            cout<<endl;

    }


    //find_jams(a,n,1);
    //cout << "Case #1" << k << ": "<< moves<< endl;

	return 0;
}
