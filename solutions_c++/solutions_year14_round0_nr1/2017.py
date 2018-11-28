#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include  <list>
using namespace std;

int main () {
  int maxtests;
  ifstream myfile ("input.txt");
  if (myfile.is_open())
  {
    myfile >> maxtests;
    list<string> results;
    for(int i = 1; i <= maxtests; i++)
    {
        int row;
        myfile >> row;
        int set1[4];
        int a;
        int count = 1;
        while(count < 5)
        {
            if(count == row)
            {
                myfile >> set1[0] >> set1[1] >> set1[2] >> set1[3];
            }
            else
            {
                myfile >> a >> a >> a >> a;
            }
            
            count ++;
        }

        myfile >> row;
        int set2[4];
        count = 1;
        while(count <5)
        {
            if(count == row)
            {
                myfile >> set2[0] >> set2[1] >> set2[2] >> set2[3];
            }
            else 
            {
                myfile >> a >> a >> a >> a;
            }
            count ++;
        }
        
       // cout <<  set1[0] << set1[1] << set1[2] << set1[3] << endl;
        //cout << set2[0] << set2[1] << set2[2] << set2[3] << endl;
    
        vector<int> v(8);
        std::vector<int>::iterator it;
        sort(set1,set1+4);
        sort(set2,set2+4);

        it=set_intersection (set1, set1 +4, set2, set2 +4, v.begin());
        v.resize(it-v.begin());

        if(v.size() > 1)
        {
            
            results.push_back("Bad magician!");
        }
        else if (v.size() == 1)
        {
            results.push_back(to_string(v.front()));
        }
        else
        {
            results.push_back("Volunteer cheated!");
        }
        
    }
    for(int i = 1; i <= maxtests; i++)
    {
        cout << "Case #" << i << ": " << results.front() << endl;
        results.pop_front();
    }
    myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}