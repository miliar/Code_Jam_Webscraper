/*
  nirmankarta
  tomorrow will be kinder

 */

#include <iostream>
#include <stdio.h>
#include <conio.h>
#define N 4

#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)

using namespace std;

int t;
int A[4][4], B[4][4],a, b;
int x[4],y[4],z[4];
int i,j,k,c,pos;
int arr[2009];
int main() {
	//freopen("a.txt", "rt", stdin);
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);

	cin >> t;
	rep(k,t)
	{
            cin>>a;
            a--;
            rep(i,N)
                    rep(j,N)
                            cin>>A[i][j];
             rep(i,N)
                x[i]=A[a][i];
            /*rep(i,N)
                cout<<x[i]<<' ';
                cout<<endl;
                /*cout<<a<<endl;
            rep(i,N)
            {
                    rep(j,N)
                            cout<<A[i][j]<<' ';
                    cout<<endl;
            }*/

            cin>>b;
            b--;
            rep(i,N)
                    rep(j,N)
                            cin>>B[i][j];
            rep(i,N)
                y[i]=B[b][i];
            /*rep(i,N)
                cout<<y[i]<<' ';
                cout<<endl;
            /*cout<<b<<endl;
            rep(i,N)
            {
                    rep(j,N)
                            cout<<B[i][j]<<' ';
                    cout<<endl;
            }*/
            rep(i,N)
                z[i]=0;
            rep(i,N)
                rep(j,N)
                    if(x[i]==y[j])
                        z[i]++;
            c=pos=0;
            rep(i,N)
                if(z[i])
                {
                    c++;
                    pos=i;
                }
            //rep(i,N)                cout<<x[i]<<' '<<z[i]<<endl;
            cout<<"Case #"<<k+1<<": ";
            if(c==1)
                cout<<x[pos]<<endl;
            else if(c>1)
                cout<<"Bad magician!"<<endl;
            else
                cout<<"Volunteer cheated!"<<endl;
    }
	return 0;
}
