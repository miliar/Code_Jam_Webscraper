using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

#define foreach(x, v) for (typeof (v).begin() x=(v).begin(); x !=(v).end(); ++x)
#define For(i,a,b) for (int i=(a); i<(b); ++i)
#define D(x) cout << #x " is " << x << endl
#define pf printf
#define sf scanf
#define loop while
#define print(i) "Case "

int main()
{
    int t,cases=0;
    ifstream myfile;
    ofstream output;
    output.open("output1.txt");
    myfile.open("A-small-attempt1.in", ios::in);
    myfile>>t;
    while(t--)
    {
        int row1, row2;
        myfile>>row1;
        int mat1[4][4], mat2[4][4];
        for(int i = 0; i<4; i++)
        {
            for(int j = 0; j<4; j++)
            {
                myfile>>mat1[i][j];
            }
        }
        int ans1[4], ans2[4];
        for(int j = 0; j<4; j++)
        {
            ans1[j] = mat1[row1-1][j];
            //printf("%d\n",ans1[j]);
        }
        myfile>>row2;
        for(int i = 0; i<4; i++)
        {
            for(int j = 0; j<4; j++)
            {
                myfile>>mat2[i][j];
            }
        }
        for(int j = 0; j<4; j++)
        {
            ans2[j] = mat2[row2-1][j];
            //printf("%d\n",ans2[j]);
        }

        ///////////////////////////////
        int count = 0, tmp;
        for(int i = 0; i<4; i++)
        {
            for(int j = 0; j<4; j++)
            {
                if(ans1[i]==ans2[j])
                {
                    tmp = ans1[i];
                    count++;
                }
            }
        }
        //ofstream myfile;
        //myfile.open ("output1.txt");
        //myfile << "Writing this to a file.\n";
        if(count == 1)
        {
            output<<"Case #"<<++cases<<": "<<tmp<<endl;
        }
        else if(count == 0)
        {
            output<<"Case #"<<++cases<<": Volunteer cheated!"<<endl;
        }
        else
        {
            output<<"Case #"<<++cases<<": Bad magician!"<<endl;
        }
    }
    myfile.close();
    output.close();
    return 0;
}
