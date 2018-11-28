#include <iostream>
#include <fstream>
#include <string>
#include <deque>
#include <stdlib.h>
#include <list>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <algorithm>
#include <climits>
#include <math.h>


using namespace std;

int dp(int A, int i, int &N, vector<int> &motes, int res){

    if (i==N || res>N ){return res;}
    else{
        if (A>motes[i]){
            A+=motes[i];
            return dp(A,i+1,N,motes,res);
        }else{
            res++;
            return min(dp((A+A-1),i,N,motes,res),dp(A,i+1,N,motes,res));
        }
    }
}


int main()
{
    ifstream input;
	//input.open("input.txt");
	input.open("A-small-attempt1.in");

	ofstream output("output.txt");
	int casenum;
    input >> casenum;

    //for each case
	for (int k=0;k<casenum;k++){
        int A=0;
        int N=0;
        int res=0;
        input >> A;
        input >> N;
        vector<int> motes;
        for (int i=0;i<N;i++){
            int m;
            input >> m;
            motes.push_back(m);
        }
        sort(motes.begin(),motes.end());


        int i;
        for (i=0;i<N;i++){
            if (A>motes[i]){
                A+=motes[i];
            }else{
                break;
            }
        }

        if(i==N){
            output << "Case #" << k+1 << ": " << 0 <<endl;
        }else{

            res = dp(A,i,N,motes,0);

            output << "Case #" << k+1 << ": " << res <<endl;
        }
	}

    input.close();
    output.close();
    return 0;
}
