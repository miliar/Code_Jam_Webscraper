#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<fstream>
#include<sstream>
using namespace std;

long long toLong(string s)
{
    stringstream ss(s);
    long long ret ;
    ss >> ret;
    return ret;   
}
int main()
{
    int T;
    ifstream in("in.txt");
    ofstream out("out.txt");
    in >> T; 
    for (int t = 1; t <= T; t++)
    {
        int N;
        in >> N;
        int X;
        in >> X;
        vector<int> v;
        
        for(int i = 0; i < N; i++)
        {
            int a;
            in >> a;
            v.push_back(a);
        }
        sort(v.begin(), v.end());
        reverse(v.begin(), v.end());
        int count = 0; 
        int total = 0;
        int cur = X;

        int good = 1;
        while(good)
        {
            
            for(int i = 0; i < v.size(); i++)
            {
                if(v[i] < 10000000) good = 0;
                if(v[i] <= cur)
                {
                    count++;
                    cur -= v[i];
                    v[i] = 10000000;
                    if(count == 2)
                    {
                            total++;
                            count = 0;
                            cur = X; 
                            i = 0;
                    }
                } 
            }
            if(count)
            {
                total++;
                count = 0;
                cur = X; 
            }
            good = !good;
        }
        out << "Case #" << t <<": " << total << endl;
        v.clear();
    }
    return 0;
}
