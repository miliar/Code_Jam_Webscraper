#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <fstream>
using namespace std;
string B;
vector<string> all;
void printB(long long int n)
    {
        for(int i = 0; i < pow(2,n); i++)
        {
            B = "";
            int temp = i;
            for (int j = 0; j < n; j++)
            {
                if (temp%2 == 1)
                    B = '1'+B;
                else
                    B = '0'+B;
                    temp = temp/2;
            }
            all.push_back(B);
         }
    }

long long int checkprime(long long int N)
{
    long long int high=sqrt(N)+1,flag=0,i=2;

    while(i<=high)
    {
        if(N%i==0)
        {
            flag=i;
            break;
        }
        else
            i++;
    }

   return flag;
}

long long int pow1(long long int i,long long int n)
{

    if(n==1)
    {
        return i;
    }
    else
    {

        long long int ans=1;
        while(n>=1)
        {
            ans=ans*i;
            n--;
        }
        return ans;
    }
}
int main()
{
    long long int T,N,J,j,k,i;
    cin >>T;
    cin >>N>>J;
    ofstream file1;
    file1.open("E.txt");
    file1<<"Case #1:"<<endl;
    printB(N);

    long long int count=0;

    for(i=all.size()-1;i>=0 && count<J;i--)
    {
        vector<long long int> ans;
         cout <<all[i]<<" ";
        for(j=2;j<=10;j++)
        {
            long long int temp=0;
            for(k=N-1;k>=0;k--)
            {
                    int val=(int)all[i][k]-48;
                    temp=temp+pow1(j,N-1-k)*val;
            }

            long long int flag=checkprime(temp);

            cout <<temp<<" ";
            /*cout <<all[i]<<" "<<temp<<" "<<flag<<endl;*/
            if(flag!=0)
                ans.push_back(flag);

        }

        cout <<endl;
        if(ans.size()==9 && all[i][0]=='1' && all[i][N-1]=='1')
        {

            file1<<all[i]<<" ";
            for(k=0;k<9;k++)
                file1<<ans[k]<<" ";
            file1<<endl;
            count++;
        }

    }


    return 0;
}
