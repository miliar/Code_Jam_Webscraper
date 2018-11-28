#include<iostream>
#include<string>
using namespace std;
//int count=0;
/*int check(int *arr, int len)
{
        int negc=0;
        for( int k=0;k<len;k++)
        {
                if(k[arr]==1)
                continue;
                else
                 negc+=1;
        }
        if(negc==len)
        return 2;
        else if(negc==0)
        return 1;
        else
        return 0;
}
*/
void transform(int *arr,int len)
{
        int i=0,j=len;
//      cout<<"Hi";
        while(i<j)
        {
                int temp=-1*arr[i];
                arr[i]=-1*arr[j];
                arr[j]=temp;
                i++;j--;
        }
        if(i==j)
        {
                arr[j]*=-1;
        }
//      count=count+1;
//      cout<<"Hello";
}
int calc(int *arr, int len)
{
        int i=0, count=0;
        while(i<len)
        {
            if (arr[i]==-1&& i==(len-1))
                    count+=1;
                else if(arr[i]==-1&&arr[i+1]==1)
                    {
                    transform(arr,i);count++;}
                    else if(arr[i]==1&&arr[i+1]==-1)
                    {
                    transform(arr,i);count++;}
                i++;
        }
        return count;
}
int main(void)
{       int test;int p=0;
        cin>>test;
        string input[test];
        cin.sync();
        while(p<test)
        {
                //cin.sync();
                cin>>input[p];
                //cout<<input[p]<<endl;
                p++;

        }        
        p=0;
        while(p<test)
        {
            
                int *arr=new int[input[p].size()];
                for(int i=0;i<input[p].size();i++)
                {
                        if(input[p].at(i)=='+')
                        arr[i]=1;
                        else
                        arr[i]=-1;
                }
                cout<<"Case #"<<p+1<<":"<<calc(arr,input[p].size())<<endl;
                p++;
         }
}