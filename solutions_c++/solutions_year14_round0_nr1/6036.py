//darshan.sonde
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <map>
#include <cstdlib>

using namespace std;

typedef vector<int> VI;
typedef long long LL;

string processTestCase(long long t);

template<typename T>
std::ostream &operator <<(std::ostream &os, const std::vector<T> &v) {
    using namespace std;
    copy(v.begin(), v.end(), ostream_iterator<T>(os, " "));
    return os;
}

int main(int argc, char **argv)
{
    long long testcases;
    cin >> testcases;
    
    for(long long t=1;t<=testcases;t++) {
        string output =  processTestCase(t);
        cout << "Case #" << t << ": " << output << endl;
    }
    return 0;
}

//============================================


string processTestCase(long long t)
{
    string res;
    
    int answer1;
    cin >> answer1;

    vector<int> answers1;
    for(int i=0;i<16;i++) {
        int a;
        cin >> a;
        answers1.push_back(a);
    }

    int answer2;
    cin >> answer2;

    vector<int> answers2;
    for(int i=0;i<16;i++) {
        int a;
        cin >> a;
        answers2.push_back(a);
    }

    int matches=0;
    int match=-1;
    for(int a1=(answer1-1)*4;a1<(answer1*4);a1++) {
        for(int a2=(answer2-1)*4;a2<(answer2*4);a2++) {
            if(answers1[a1]==answers2[a2])  {
                matches++;
                match=answers1[a1];
            }
        }
    }

    if(matches == 1) {
        res.append(to_string(match));
    }else if(matches==0) {
        res.append("Volunteer cheated!");
    }else {
        res.append("Bad magician!");
    }
    
    return res;
}

