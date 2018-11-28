#include <iostream>
#include <stdio.h>
#include <string.h>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

vector<double> blocks1;
vector<double> blocks2;

bool cmp(double a,double b)
{
    return a>b;
}

int ansok2(vector<double> blocks1, vector<double> blocks2)
{
    int ans2 = 0;
    while(blocks1.size() != 0)
        {
            if(blocks1[0] > blocks2[0]){ans2++;blocks1.erase(blocks1.begin());}
            else {
                blocks1.erase(blocks1.begin());
                blocks2.erase(blocks2.begin());
            }
        }
        return ans2;
}
int ok(const vector<double>& b1,const vector<double>& b2)
{
    int sum = 0;
    for(int i = 0 ; i < b1.size() ; i++)
    {
        if(b1[i] > b2[i])sum++;
    }
    return sum;
}

void print(const vector<double>& b)
{
    for(int i = 0 ; i < b.size() ; i++)
        cout << b[i] << " ";
    cout << endl;
}
int main()
{
    int t;
    int n,ans1,ans2;
    double w;
    fstream fs;
    FILE* fso;
    fs.open("C:\\D-large.in");
    fso = fopen("C:\\A-small-attempt0.out","w");
    fs >> t;
    //cin >> t;
    for(int count = 1; count <= t ; count++)
    {
        blocks1.clear();
        blocks2.clear();
        fs >> n;
       // cin >> n;
        for(int i = 0 ; i < n ;i++){
               // cin >> w;
                fs >> w;
                blocks1.push_back(w);
        }
        for(int i = 0 ; i < n ;i++){
               // cin >> w;
                fs >> w;
                blocks2.push_back(w);
        }

        sort(blocks1.begin(),blocks1.end(),cmp);
        sort(blocks2.begin(),blocks2.end(),cmp);

        //print(blocks1);
        //print(blocks2);

        ans2 = ansok2(blocks1,blocks2);

        //print(blocks1);
        //print(blocks2);

        while(ok(blocks1,blocks2) != blocks1.size()){
            blocks1.erase(blocks1.end()-1);
            blocks2.erase(blocks2.begin());

          //  print(blocks1);
          //  print(blocks2);
        }

        //print(blocks1);
        //print(blocks2);

        ans1 = blocks1.size();

        //printf("Case #%d: %d %d\n",count,ans1,ans2);
        fprintf(fso,"Case #%d: %d %d\n",count,ans1,ans2);
    }
    return 0;
}
