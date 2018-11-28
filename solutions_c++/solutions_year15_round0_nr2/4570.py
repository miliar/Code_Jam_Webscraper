#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <climits>
#include <sstream>
#include <iterator>
#include <algorithm>
using namespace std;

int recursionReduce(vector<int>pancakes);
int main (){
    string line;
    int N;
    ifstream input ("B-small-attempt3.in");
    ofstream output ("p2.out");
    if (input.is_open()){
        getline (input, line);
        stringstream (line) >> N;
        for (int i = 0; i < N; i++){
            int numDiners;
            getline (input, line);
            stringstream (line) >> numDiners;
            getline (input, line);
            istringstream iss(line);
            vector<int> pancakes{istream_iterator<int>{iss}, istream_iterator<int>{}};
            output <<"Case #" << i+1 << ": " << recursionReduce (pancakes) << endl;
        }
    }
    return 0;
}


int recursionReduce(vector<int>pancakes){
    sort (pancakes.begin(),pancakes.end(),std::greater<int>());
    //bool reducedAlready[1000] = {0};
    int highestValue = -1;
    int lowestValue = INT_MAX;
    for (int i = 0; i < pancakes.size();i++){
//        cout << pancakes[i]<< " ";
        if (pancakes[i] > highestValue)
            highestValue = pancakes[i];
        if (pancakes[i] < lowestValue)
            lowestValue = pancakes[i];
    }
//    cout <<endl<<"HIGHEST"<<highestValue<<endl;
    if (highestValue <= 3){
        return highestValue;
    }
    int lowestTime = highestValue;
    int currTime;
    //for (int i = 0; i < pancakes.size(); i++){
        if (pancakes[0] >3 /*&& !reducedAlready[pancakes[0]]*/){
            //reducedAlready[pancakes[0]]=true;
            for (int j = 2; j*j <= pancakes[0]; j++){
                vector<int>newPancakes = pancakes;
//                for (int k = 0; k < newPancakes.size(); k++){
//                    if (k==i&&i!=0)cout << ">";
//                    cout << newPancakes[k];
//                    if (k==i)cout << "<";
//                    else if (k!=i-1) cout << " ";
//                }

                newPancakes.push_back (newPancakes[0]/j);
                newPancakes[0]= newPancakes[0] - (newPancakes[0]/j);
//                cout <<endl;
                currTime = 1+recursionReduce (newPancakes);
                if (currTime < lowestTime){
                    lowestTime = currTime;
                }
            }

        }
//        if (lowestTime >= highestValue){
//            break;
//        }
    //}
    return lowestTime;
}
