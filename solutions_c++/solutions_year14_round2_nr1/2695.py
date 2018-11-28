#include <future>
#include <cmath>

#include <iostream>
#include <iomanip>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <deque>
#include <algorithm>
#include <iterator>
#include <boost/shared_ptr.hpp>
#include <boost/shared_array.hpp>
#include <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/vector.hpp>
#include <boost/numeric/ublas/io.hpp>
#include <boost/random/mersenne_twister.hpp>
#include <boost/random/uniform_int_distribution.hpp>
#include <boost/multi_array.hpp>

using namespace std;

int main(int argc, char* argv[])
{
    int tests;
    cin >> tests;
    vector<future<uint64_t>> results(tests);
    for (int i = 0; i < tests; ++i)
    {
        int n;
        cin >> n;
        string base;
        string d;
        cin >> d;
        vector<multiset<int> > data;
        //vector<vector<int> > data;
        {
            char last = 0;
            int count=0;
            
            for (auto it = d.begin(); it != d.end(); ++it)
            {
                if (last == *it)
                {
                    ++count;
                }
                else
                {
                    if (last)
                    {
                        multiset<int> s;
                        s.insert(count);
                        data.push_back(s);
                    }
                    base.push_back(*it);

                    last = *it;
                    count = 1;
                }
            }
            if (last)
            {
                multiset<int> s;
                s.insert(count);
                data.push_back(s);
            }
        }
        bool ok=true;
        for (int j=1; j<n; ++j)
        {
            cin >> d;
//cerr << "X:" << d << "," << base << endl;
            char last = 0;
            int count=0;
            auto bit = base.begin();
            auto dit = data.begin();
            for (auto it = d.begin(); it != d.end(); ++it)
            {
                if (last == *it)
                {
                    ++count;
                }
                else
                {
                    if (*it != *bit)
                    {
                        ok=false;
                        j=n;
                        break;
                    }
                    if (last)
                    {
                        dit->insert(count);
                    ++dit;
                    }
                    ++bit;
                    last = *it;
                    count = 1;
                }
            }
            if (last)
            {
                dit->insert(count);
            }
            if (bit != base.end())
            {
//cerr<<"Z"<< j<<endl;
ok = false;
                j=n;
                break;
            }
        }
//cerr<<"X"<< data.size() << endl;
/*
 * for (auto it=data.begin();it!= data.end();++it)
            {
                for (auto dit=it->begin();dit!=it->end();++dit)
                {
                    cerr << *dit<<" ";
                }
                    cerr <<"]" <<endl;
            }
*/
        cout << "Case #" << i+1 << ": ";
        if (!ok) cout << "Fegla Won" << endl;
        else
        {
            int result = 0;
            for (auto it=data.begin();it!= data.end();++it)
            {
                auto m = it->begin();
                int size=it->size();
//cerr<<"A"<< size <<endl;
if (size == 1) ;
else if (size%1)
                {
                    size /= 2;
                    for (int x=0;x<size;++x) ++m;
                    int median= *m;
                    for (auto dit=it->begin();dit!=m;++dit)
                    {
                        result += median - *dit;
                    }
                    ++m;
                    for (auto dit=m;dit!=it->end();++dit)
                    {
                        result += *dit - median;
                    }
                }
                else if (size==2)
                {
//cerr<<"B"<< endl;
                    int a1=*m;
                    ++m;
                    int a2=*m;
                    result += a2-a1;
                }
                else
                {
                    int r1=0;
                    int r2=0;
                    size /= 2;
                    --size;
//cerr<<"C"<< size <<endl;
                    for (int x=0;x<size;++x) ++m;
                    int median= *m;
                    for (auto dit=it->begin();dit!=m;++dit)
                    {
                        r1 += median - *dit;
                    }
                    ++m;
                    for (auto dit=m;dit!=it->end();++dit)
                    {
                        r1 += *dit - median;
                    }
                    median= *m;
                    for (auto dit=it->begin();dit!=m;++dit)
                    {
                        r2 += median - *dit;
                    }
                    ++m;
                    for (auto dit=m;dit!=it->end();++dit)
                    {
                        r2 += *dit - median;
                    }
                    if (r1>r2) result+=r2;
                    else result += r1;
//cerr << r1 << ":" << r2 << endl;
                }
            }
            cout << result << endl;
        }
    }
    return 0;
}

