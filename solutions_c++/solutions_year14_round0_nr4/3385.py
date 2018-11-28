#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int T,n;

void print(const vector<double> a)
{
    for(int i=0;i<n;i++)
        cout<<a[i]<<" ";
    cout<<endl;
}

int war1(vector<double> a, vector<double> b)
{
    sort(a.begin(), a.end());
    sort(b.begin(), b.end(), std::greater<double>());
        
    int score = 0;
    for(int i=0;i<n;i++)
    {
        if(a.front() > b.back())
        {
            score ++;
            a.erase(a.begin());
            b.pop_back();
        }
        else
        {
            a.erase(a.begin());
            b.erase(b.begin());
        }
    }
    
    return score;
}

int war2(vector<double> a, vector<double> b)
{
    sort(a.begin(), a.end(), std::greater<double>());
    sort(b.begin(), b.end(), std::greater<double>());
    
    int score = 0;
    for(int i=0;i<n;i++)
    {
        if(a[0] > b[0])
        {
            score ++;
            a.erase(a.begin());
            b.pop_back();
        }
        else
        {
            a.erase(a.begin());
            b.erase(b.begin());
        }
    }
    
    return score;
}

int main()
{
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cin>>n;
        vector<double> a, b;
        double temp;
        for(int i=0;i<n;i++)
        {
            cin>>temp;
            a.push_back(temp);
        }
        for(int i=0;i<n;i++)
        {
            cin>>temp;
            b.push_back(temp);
        }
        
        int w1 = war1(a,b);
        int w2 = war2(a,b);
        
        cout<<"Case #"<<t<<": "<<w1<<" "<<w2<<endl;
    }
}