#include<fstream>
#include<string.h>
#include<string>
#include<math.h>

using namespace std;

int fq1[150],fq2[150],sz1[150],sz2[150];

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("A-small-attempt2.in");
    fout.open("output2.txt");
    int T,N,i,count,k,x,y;
    fin>>T;
    for(k=1;k<=T;k++)
    {
        count=x=y=0;
        fin>>N;
        string s1,s2,s3="",s4="";
        int l1,l2,l3,l4;
        memset(fq1,0,sizeof(fq1));
        memset(fq2,0,sizeof(fq2));
        memset(sz1,0,sizeof(sz1));
        memset(sz2,0,sizeof(sz2));
        fin>>s1>>s2;
        l1=s1.length();
        l2=s2.length();
        for(i=0;i<l1-1;i++)
        {
            if(s1[i]==s1[i+1])
            sz1[(int)(s1[i])]++;
            else
            {
                sz1[(int)(s1[i])]++;
                fq1[x++]=sz1[(int)(s1[i])];
                sz1[(int)(s1[i])]=0;
            }
        }
        sz1[(int)(s1[l1-1])]++;
        fq1[x++]=sz1[(int)(s1[l1-1])];
        for(i=0;i<l2-1;i++)
        {
            if(s2[i]==s2[i+1])
            sz2[(int)(s2[i])]++;
            else
            {
                sz2[(int)(s2[i])]++;
                fq2[y++]=sz2[(int)(s2[i])];
                sz2[(int)(s2[i])]=0;
            }
        }
        sz2[(int)(s2[l2-1])]++;
        fq2[y++]=sz2[(int)(s2[l2-1])];
        for(i=0;i<l1-1;i++)
        {
            if(s1[i]!=s1[i+1])
            s3+=s1[i];
        }
        s3+=s1[l1-1];
        for(i=0;i<l2-1;i++)
        {
            if(s2[i]!=s2[i+1])
            s4+=s2[i];
        }
        s4+=s2[l2-1];
        l3=s3.length();
        l4=s4.length();
        if(s3==s4)
        {
            for(i=0;i<l3;i++)
            {
                count+=fabs(fq1[i]-fq2[i]);
            }
            fout<<"Case #"<<k<<": "<<count<<endl;
        }
        else
        fout<<"Case #"<<k<<": Fegla Won\n";
    }
    return 0;
}
