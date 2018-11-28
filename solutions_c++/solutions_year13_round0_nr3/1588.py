#include <iostream>
#include <fstream>
#include <cmath>
#include <sstream>
#include <algorithm>

using namespace std;

fstream file;
long long square;
static long long arr[50];

bool palin_string(string s)
{
    string t;
    t=s;
    reverse(t.begin(),t.end());

    return s==t;
}

string toString(long long n)
{
    ostringstream ost;
    ost<<n;
    ost.flush();
    return ost.str();
}

void calc (int low, int high)
{
    long long count=0;
    for(long long i=low;i<=high;i++)
    {
            string temp=toString(i);
            if(palin_string(temp))
            {
                square=i*i;
                temp=toString(square);
                if(palin_string(temp))
                {
                    arr[count]=square;
                    count++;
                }
            }
    }
}

int count (long long low, long long high)
{
    int tot=0;
    for(int i=0;i<39;i++)
    {
        if(arr[i]>high)return tot;
        if(arr[i]<low)continue;

        if(arr[i]>=low&&arr[i]<=high)tot++;
    }
    return tot;
}

int main()
{
    ofstream answer;
    file.open("C-large-1.in");
    answer.open("answer.txt");

    int n=0;
    while(int temp=file.get())
    {
        if(temp==10)break;
        temp-=48;
        n=(n*10)+temp;
    }
    //cout<<n<<endl;
    long long low=1,high=10000000,total=0;
    calc(low,high);

    for(int i=1;i<=n;i++)
    {
       file>>low;
       file>>high;

       int total=0;
       total=count(low,high);

       //cout<<"Case #"<<i<<": "<<total<<endl;
       answer<<"Case #"<<i<<": "<<total<<endl;
    }

}
