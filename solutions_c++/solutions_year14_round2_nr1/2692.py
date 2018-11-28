#include <iostream>
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <numeric>
#include <iterator>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <string>

#define mp make_pair
#define pb push_back
#define sqr(x) ((x)*(x))
#define foreach(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef vector<bool> VB;
typedef vector<VB> VVB;

template<typename T> int size(const T &a) { return a.size(); } 


void process(void) {
    int n, result = 0;
    scanf("%d", &n);
    vector<string> a(n);
    vector< vector<int> > countVector(n);
    vector<char> b;
    vector<int> letterCount;
    for (int i = 0; i < n; ++i)
    {
        cin >> a[i];
    }
    
    //process letters
    int j = 0;
    b.push_back(a[0][0]);
    while (char c = a[0][j]){
        if (c != b.back()) b.push_back(c);
        j++;
    }

    // process other words
    for (int i = 0; i < n; ++i)
    {
        // store characters in each string
        int j = 0; //index into string
        int letterIndex = 0; //index into letterArray
        int tempCount = 0;
        vector<int> tempStore; //store count
        // process first word
        while(char c = a[i][j]){
            // cout << "c is " << c << " letter is " << b[letterIndex] <<endl;
            if (c==b[letterIndex])
            {
                tempCount++;
            }
            else if((j == 0) || (c!=b[letterIndex+1])){
                cout << "Fegla Won\n";
                return;
            }
            else {
                tempStore.push_back(tempCount);
                tempCount = 1;
                letterIndex++;
            }
            j++;
        }
        if(letterIndex!=b.size()-1){
            cout << "Fegla Won\n";
            return;
        }
        tempStore.push_back(tempCount); // store the last count
        countVector[i]=(tempStore);
    }

    for (int i = 0; i < b.size(); ++i)
    {
        int totalCount = 0;
        for (int j = 0; j < n; ++j)
        {
            totalCount += countVector[j][i];
        }
        int r = totalCount % n;
        int average = (r <= n/2) ? totalCount/n: totalCount/n + 1;
        // int result = 0;
        for (int j = 0; j < n; ++j)
        {
            result += abs(countVector[j][i]-average);
        }
    }

    cout << result << endl;
}

int main(void)
{
    // precalc();
    int T;
    scanf("%d", &T);
    for(int i=1;i<=T;i++) {
        printf("Case #%d: ", i);
        process();
    }
}