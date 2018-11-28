#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;
int main(){
    int ti;
    char ch;
    int n,m,sum,yuan,negi,negk,posi,posk;
    int a[5][5];
    int en[20000],st[20000],sign1[20000],sign2[20000],b[20000];
    int ans;
    bool flag;
    ifstream fin;
    ofstream fout;
    fin.open("in.txt");
    fout.open("out.txt");
    fin>>ti;
    a[1][1]=1;a[1][2]=2;a[1][3]=3;a[1][4]=4;
    a[2][1]=2;a[2][2]=-1;a[2][3]=4;a[2][4]=-3;
    a[3][1]=3;a[3][2]=-4;a[3][3]=-1;a[3][4]=2;
    a[4][1]=4;a[4][2]=3;a[4][3]=-2;a[4][4]=-1;
    for (int i=0; i < ti; i++)
    {
        fin>>n>>m;fin.get(ch);
        for(int j=0;j<n;j++)
        {
            fin.get(ch);
            if(ch=='i') b[j]=2;else
            if(ch=='j') b[j]=3;else
            b[j]=4;

        }


        for (int j=n;j<n*m;j++)
            b[j]=b[j-n];
            st[0]=b[0];
        sign1[0]=1;

        for (int j=1;j<m*n;j++)
        {
            st[j]=a[st[j-1]][b[j]];
            if (st[j]<0) sign1[j] = sign1[j-1]*-1;else sign1[j]=sign1[j-1];
            st[j]=abs(st[j]);
        }
        en[m*n-1]=b[m*n-1];
        sign2[m*n-1]=1;

        for (int j=m*n-2;j>=0;j--)
        {
            en[j]=a[b[j]][en[j+1]];
            if (en[j]<0) sign2[j] = sign2[j+1]*-1;else sign2[j]=sign2[j+1];
            en[j]=abs(en[j]);


        }
        flag =false;

        if (st[m*n-1]*sign1[m*n-1]==-1){
posk=-1;posi=-1;
        for (int j=0;j<m*n;j++)
        {
           if (st[j]*sign1[j]==2) {
            posi=j;
            break;
           }
        }

        for (int j=m*n-1;j>=0;j--)
        {
            if(en[j]*sign2[j]==4){
                posk=j;
                break;
            }

        }
        if(posk>=0 && posi>=0)
        if (posk>posi) flag = true;
        }

        if (flag)fout<<"Case #"<<i+1<<": "<<"YES"<<endl; else fout<<"Case #"<<i+1<<": "<<"NO"<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
