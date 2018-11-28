#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int getRes(int &ans1, int &ans2,  vector<vector<int> > &mp1, vector<vector<int> > &mp2){

    vector<int> a = mp1[ans1-1];
    vector<int> b = mp2[ans2-1];

    vector<int> v(8,0);
    vector<int>::iterator it;

    sort(a.begin(),a.end());
    sort(b.begin(),b.end());

    it  = set_intersection(a.begin(),a.end(),b.begin(),b.end(),v.begin());
    v.resize(it-v.begin());


    if (v.size()==0){
        return -1;
    }
    if (v.size()==1){
        return v[0];
    }

    if (v.size()>1){
        return 0;
    }
}

int main()
{
    ifstream input;
	input.open("A-small-attempt0.in");
	ofstream output("outputl.txt");
	int casenum;
	input >> casenum;
	//for each case
	for (int k=0;k<casenum;k++){
        int ans1;
        int ans2;
        vector<vector<int> > mp1(4,vector<int>(4,0));
        vector<vector<int> > mp2(4,vector<int>(4,0));
        input >> ans1;
        for (int i=0;i<4;i++){
            for (int j=0;j<4;j++){
                input >> mp1[i][j];
            }
        }
        input >>ans2;
        for (int i=0;i<4;i++){
            for (int j=0;j<4;j++){
                input >> mp2[i][j];
            }
        }

      int res = getRes(ans1,ans2,mp1,mp2);


        if (res == -1){
            output << "Case #" << k+1 << ": " << "Volunteer cheated!" << endl;
        }else{
            if (res==0){
                output << "Case #" << k+1 << ": " << "Bad magician!" << endl;
            }else{
                output << "Case #" << k+1 << ": " << res << endl;
            }
        }

	}

    input.close();
	output.close();
    return 0;
}
