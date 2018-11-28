#include<fstream>
using namespace std;
int T,N,*P,tot;
char *temp;
    void srt()
    {
        int i,j,k;
        for(j=0;j<N;j++)
            for(k=j;k<N;k++)
                if(P[j]<P[k])
                {
                    P[j]+=P[k];
                    P[k]=P[j]-P[k];
                    P[j]=P[j]-P[k];
                    temp[j]+=temp[k];
                    temp[k]=temp[j]-temp[k];
                    temp[j]=temp[j]-temp[k];
                }
    }
    int chck()
    {
       int flag=0,i,j;
       for(i=0;i<N-1;i++)
       {
           if(P[i]!=P[i+1])
           {
               flag=1;
               break;
           }
       }
       return flag;
    }
int main()
{
    int i,j,k,grt=0,grti,flag=1;
    char **ans;
    ifstream fin("A-small-attempt1.in");
    ofstream fout("output.in");
    fin>>T;
    for(i=0;i<T;i++)
    {
        fin>>N;
        P=new int [N];
        tot=0;
        temp=new char [N];
        ans=new char *;
        for(j=0;j<N;j++)
        {
            fin>>P[j];
            tot+=P[j];
            temp[j]=j+65;
        }
        j=0;
        flag=1;
        fout<<"Case #"<<i+1<<": ";
        while(flag)
        {
            srt();
            if(chck()==1){
                while(chck()==1)
                {
                    if(P[1]!=P[2]){
                    ans[j]=new char;
                    ans[j][0]=temp[0];
                    ans[j][1]=temp[1];
                    ans[j][2]=NULL;
                    P[1]--;
                    P[0]--;
                    tot-=2;
                    fout<<temp[0]<<temp[1]<<' ';
                    j++;
                    }
                    else
                    {
                        ans[j]=new char;
                        ans[j][0]=temp[0];
                        ans[j][1]=temp[0];
                        ans[j][2]=NULL;
                        P[0]-=2;
                        tot-=2;
                        fout<<temp[0]<<temp[0]<<' ';
                        j++;
                    }
            srt();
                }
            //cout<<"doing1";
            }
            else if(chck()==0&&P[0]==0)
                    flag=0;
            else if(chck()==0)
            {
                    if(N%2)
                    {
                        ans[j]=new char;
                        ans[j][0]=temp[0];
                        ans[j][1]=NULL;
                        P[0]--;
                        tot-=1;
                        fout<<temp[0]<<' ';
                        j++;
                    }
                    else
                    {

                        ans[j]=new char;
                        ans[j][0]=temp[0];
                        ans[j][1]=temp[1];
                        ans[j][2]=NULL;
                        P[1]--;
                        P[0]--;
                        tot-=2;
                        fout<<temp[0]<<temp[1]<<' ';
                        j++;
                    }
            }
        }
            fout<<endl;
        delete temp;
        delete ans;
        delete P;
    }
}
