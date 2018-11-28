#include<iostream>
using namespace std;

int main()
{
    int t,c,n,m,j,i,a,inp[101][101],chk,k,subchk1,subchk2;
    cin>>t;
    for(c=1;c<=t;c++)
    {
        cin >> n >> m;
        for (j=0;j<n;j++)
        {
            for(i=0;i<m;i++)
            {
                cin>>inp[j][i];
                //a[j][i]=0;
            }
        }
        //for(j=0;j<n;j++)a[j][0]=1;
        //for(i=0;i<m;i++)a[0][i]=1;
        chk=1;
        for (j=0;j<n&&chk;j++)
        {
            for(i=0;i<m&&chk;i++)
            {
                a=inp[j][i];
                subchk1=1;
                subchk2=1;
                for(k=0;k<n;k++)
                    if (a<inp[k][i])
                    {
                        subchk1=0;
                        break;
                    }
                for(k=0;k<m;k++)
                    if (a<inp[j][k])
                    {
                        subchk2=0;
                        break;
                    }
                if(subchk1==0 && subchk2==0)chk=0;
            }
        }

        cout << "Case #"<<c<<": ";
        if(chk)cout << "YES"<<endl;
        else cout << "NO"<<endl;

    }


}
