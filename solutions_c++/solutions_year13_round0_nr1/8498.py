#include<string>
#include<iostream>
#include<map>
#include<vector>
using namespace std;
int main()
{
    int n,i,j,k;
    char arr[4][4];
    map<string,int> f;
    f["XXXT"]=1;
    f["XXTX"]=1;
    f["XTXX"]=1;
    f["TXXX"]=1;    
    f["XXXX"]=1;
    f["OOOT"]=1;
    f["OOTO"]=1;
    f["OTOO"]=1;
    f["TOOO"]=1;
    f["OOOO"]=1;
    cin>>n;
    char x[5];
    for(i=0;i<n;i++)
    {
        int flag = 0;
        int count = 0;
        for(j=0;j<4;j++)
        {
            scanf("%s",x);
            for(k=0;k<strlen(x);k++)
            {
                arr[j][k] = x[k];
                if(arr[j][k]!='.') count++;
            }
        }
        string h="";
        string str;
        //columns
        for(j=0;j<4;j++)
        {
            str="";
            for(k=0;k<4;k++)
            {
                str = str + arr[j][k];
            }
            if(f[str]) {flag = 1;h=str;break;}
        }
        //rows
        for(j=0;j<4;j++)
        {
            string str="";
            for(k=0;k<4;k++)
            {
                str = str + arr[k][j];
            }
            if(f[str]) {flag = 1;h=str;break;}
        }
        //diagonals
        str="";
        str = str + arr[0][0] + arr[1][1] + arr[2][2] + arr[3][3];
        if(f[str]) {flag = 1;h=str;}
        else
        {
            str="";
            str = str + arr[0][3] + arr[1][2] + arr[2][1] + arr[3][0];
            if(f[str]) {flag = 1;h=str;}
        }
        //check
        if(flag == 0) 
        {
            if(count ==16) cout << "Case #" << i+1 << ": Draw" << endl;
            else cout << "Case #" << i+1 << ": Game has not completed" << endl;
        }
        else
        {
            cout << "Case #" << i+1 << ": " << h[1] << " won" << endl;
        }
    }
    return 0;
}
