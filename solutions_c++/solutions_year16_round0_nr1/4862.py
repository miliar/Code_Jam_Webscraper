#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int digit,ittr,sat_cond,n;
    unsigned long int start_num,res,temp_num;
    bool check_num[10]={0};
    ifstream fin("A-large.in");
    ofstream fout("out.txt");
    fin>>n;
    for(int j=0;j<n;j++)
    {
         fin>>start_num;
         for(int y=0;y<10;y++)
          {
             check_num[y]=0;
          }
        if(start_num==0)
        {
            fout<<"Case #"<<j+1<<": "<<"INSOMNIA"<<"\n";
        }
        else
        {
            ittr=1;
            do
            {
                res=ittr*start_num;
                cout<<"\nres"<<res;
                temp_num=res;
                while(temp_num>0)
                {
                    digit=temp_num%10;
                    temp_num=temp_num/10;
                    check_num[digit]=1;
                }
                sat_cond=0;
                for(int i=0;i<10;i++)
                {
                    if(check_num[i])
                        sat_cond++;
                }
                ittr++;
                cout<<"\n sat_cond"<<sat_cond;
            }while(sat_cond!=10);
            fout<<"Case #"<<j+1<<": "<<res<<"\n";
        }
    }
    return 0;
}
