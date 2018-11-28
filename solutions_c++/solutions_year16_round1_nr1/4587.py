#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;

int main()
{
    std::ifstream infile("A-small-attempt1.in");

    ofstream outfile;
    outfile.open("Last-word.txt");

    char S[17],ans[100][17];
    int T;
    infile>>T;

    for(int i=0;i<T;i++)
    {
        infile>>S;
        int len=strlen(S);
        ans[i][0]=S[0];
        for(int j=1;j<len;j++)
        {
            if(ans[i][0]>S[j])
            {
                ans[i][j]=S[j];
            }
            else
            {
                char dumm[17]={' '};
                strcat(dumm,ans[i]);
                dumm[0]=S[j];
                strcpy(ans[i],dumm);
            }
        }
        ans[i][strlen(S)]='\0';
    }

    for(int i=0;i<T;i++)
        outfile<<"Case #"<<(i+1)<<": "<<ans[i]<<endl;

}
