#include <cstdio>
#include <cstring>
#include <fstream>
using namespace std;

int main()
{
    fstream ofile;
    fstream ifile;
    ifile.open("A-large.in",ios::in);
    ofile.open("testA.txt",ios::out);
    int T;
    int S;
    char str[1100];
    int audi[1100];
    int count =0;
    int line=1;
    ifile>>T;//scanf("%d",&T);
    while(T--)
    {
        int ans=0;
        count=0;
        memset(str,0,sizeof(str));
        memset(audi,0,sizeof(audi));
        ifile>>S>>str;//scanf("%d %s",&S,str);
        for(int i=0;i<=S;i++)
        {
            audi[i]=str[i]-'0';
            if(audi[0]==0)
            {
                ans++;
                audi[0]=1;
            }
            else if(i !=0 && i>count)
            {
                ans+=i-count;
                audi[i]+=i-count;
            }
            count+=audi[i];
        }

        //printf("Case #%d: %d\n",line++,ans);
        ofile<<"Case #"<<line++<<": "<<ans<<"\n";
    }


}
