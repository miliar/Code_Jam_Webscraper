#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <tuple>
#include <queue>
#include <map>
#include <algorithm>
#include <utility>

using namespace std;

int main()
{
	ifstream ifile;
	ofstream ofile;
	int test;
	ifile.open("A-large.in");
	ofile.open("out.txt");


    ifile>>test;
    for(int i=0;i<test;i++)
    {
        int num,pres=0,req=0;
        string str;
        stringstream ss;
        vector <int> arr;
        ifile>>num;
        ifile>>str;
        for(int j=0;j<(num+1);j++)
        {
            int temp;
            ss<<str.at(j);
            ss>>temp;
            arr.push_back(temp);
            ss.str(string());
            ss.clear();
        }
        req=0;
        for(int j=0;j<arr.size()-1;j++)
        {
//            if(pres>=((arr.at(j)%2)*j))
//            {
//                pres+=arr.at(j);
//                sum+=arr.at(j);
//            }
            pres+=arr.at(j);
            if(pres<(j+1) && (arr.at(j+1)!=0))
            {
                req+=(j+1)-pres;
                pres+=(j+1)-pres;
            }
        }
        ofile<<"Case #"<<(i+1)<<": "<<req;
        ofile<<endl;
    }
    ifile.close();
    ofile.close();
	return 0;
}
