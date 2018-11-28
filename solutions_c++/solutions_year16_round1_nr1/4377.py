#include<iostream>
#include<fstream>
using namespace std;
int main()
{
     freopen("d:/work/large.in","r",stdin);
     freopen("d:/work/outputr1.out","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        char s[1005],s1[1005];
        s1[1]='\0';
        int j=0;
        cin>>s;
        s1[0]=s[0];
        while(s[j]!='\0')
        {
            int flag=0;
            char ch=s1[0];
            do{
            if(((int)ch)<=((int)s[j+1]))
            {
                flag=1;
                break;
            }
            else
            {
                s1[j+1]=s[j+1];
                s1[j+2]='\0';
            }
            j++;
           } while(s[j]!='\0');
           if(flag==1)
           {
              int k=0;
               char rep=s1[k];
               s1[k]=s[j+1];
               while(rep!='\0')
               {
                   k++;
                    char m=s1[k];
                    s1[k]=rep;
                    rep=m;
               }
               s1[k+1]='\0';
               j++;
           }
        }
        cout<<"Case #"<<i<<": ";
        int k=0;
        while(s1[k]!='\0')
            cout<<s1[k++];
        cout<<endl;
    }
    return 0;
}
