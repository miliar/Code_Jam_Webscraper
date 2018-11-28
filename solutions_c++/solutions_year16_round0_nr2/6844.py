#include <iostream>
#include <string>
#include <bitset>
#include <queue>
#include <set>
using namespace std;


int main(int argc, char* argv[])
{
    int T;
    cin >> T;
    for(int i=0; i<T; ++i)
    {
        cout << "Case #" << i+1 << ": ";
        string pancake;
        cin >> pancake;
        bitset<100> pcbit;
        bitset<100> target;
        int psize = pancake.size();
        for(int j=0; j<psize; ++j)
        {
            if(pancake[j]=='+') pcbit[j]=1;
            target[j] = 1;
        }
        queue<bitset<100> > theQ;
        queue<int> depthQ;
        theQ.push(pcbit);
        depthQ.push(0);
        set<string> testSet;
        testSet.insert(pcbit.to_string());
        while(!theQ.empty())
        {
            bitset<100> curr = theQ.front();
            theQ.pop();
            int currDepth= depthQ.front();
            depthQ.pop();
            if(curr == target)
            {
                cout << currDepth << endl;
                break;
            }
            ++currDepth;
            for(int p=0; p<psize-1; ++p)
            {
                if(curr[p]!=curr[p+1])
                {
                    bitset<100> tryP = curr;
                    for(int z=0; z<=p; ++z)
                    {
                        tryP[z]=~curr[p-z];
                    }
                    string ss = tryP.to_string();
                    if(testSet.find(ss)==testSet.end())
                    {
                        theQ.push(tryP);
                        depthQ.push(currDepth);
                        testSet.insert(ss);
                    }
                    break;
                }
            }
            {
                bitset<100> tryP = curr;
                int p = psize -1;
                for(int z=0; z<=p; ++z)
                {
                    tryP[z]=~curr[p-z];
                }
                string ss = tryP.to_string();
                if(testSet.find(ss)==testSet.end())
                {
                    theQ.push(tryP);
                    depthQ.push(currDepth);
                    testSet.insert(ss);
                }
            }
        }
        
    }
    return 0;
}

//void test()
//{
//        string pancake;
//        cin >> pancake;
//        bitset<100> pcbit;
//        bitset<100> target;
//        int psize = pancake.size();
//        for(int j=0; j<psize; ++j)
//        {
//            if(pancake[j]=='+') pcbit[j]=1;
//            target[j] = 1;
//        }
//        queue<bitset<100> > theQ;
//        queue<int> depthQ;
//        theQ.push(pcbit);
//        depthQ.push(0);
//        set<string> testSet;
//        testSet.insert(pcbit.to_string());
//        while(!theQ.empty())
//        {
//            bitset<100> curr = theQ.front();
//            theQ.pop();
//            int currDepth= depthQ.front();
//            depthQ.pop();
//            if(curr == target)
//            {
//                cout << currDepth << endl;
//                break;
//            }
//            ++currDepth;
//            for(int p=0; p<psize; ++p)
//            {
//                bitset<100> tryP = curr;
//                for(int z=0; z<=p; ++z)
//                {
//                    tryP[z]=~curr[p-z];
//                }
//                string ss = tryP.to_string();
//                if(testSet.find(ss)==testSet.end())
//                {
//                    theQ.push(tryP);
//                    depthQ.push(currDepth);
//                    testSet.insert(ss);
//                }
//            }
//        }
//}