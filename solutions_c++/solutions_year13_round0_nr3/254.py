/*
 * main.cpp
 *
 *  Created on: 06.04.2013
 *      Author: grand
 */

#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

const int MAX_LEN = 25;
const int MAX_NORM = 4;

#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <string>

namespace Zeus
{
    namespace Numeric
    {
        class LongInt
        {
            std::vector < int > data;
            static const int base = 1000 * 1000 * 1000;
        public:
            LongInt ()
            {
            }

            LongInt (int src)
            {
                while (src)
                {
                    data.push_back(src % base);
                    src /= base;
                }
            }

            bool operator < (const LongInt & src) const
            {
                if(data.size()<src.data.size())return true;
                if(data.size()>src.data.size())return false;
                for(int i=data.size()-1; i>=0; --i)
                {
                    if(data[i]<src.data[i])return true;
                    if(data[i]>src.data[i])return false;
                }
                return false;
            }
            bool operator <= (const LongInt & src) const
            {
                if(data.size()<src.data.size())return true;
                if(data.size()>src.data.size())return false;
                for(int i=data.size()-1; i>=0; --i)
                {
                    if(data[i]<src.data[i])return true;
                    if(data[i]>src.data[i])return false;
                }
                return true;
            }

            bool operator > (const LongInt & src) const
            {
                return !operator<=(src);
            }

            bool operator >= (const LongInt & src) const
            {
                return !operator<(src);
            }

            bool operator == (const LongInt & src) const
            {
                if(data.size()!=src.data.size())return false;
                for(int i=data.size()-1; i>=0; --i)
                {
                    if(data[i]!=src.data[i])return false;
                }
                return true;
            }

            bool operator != (const LongInt & src) const
            {
                return !operator==(src);
            }

            LongInt (const std::string & src)
            {
                for (int i = (int) src.length(); i > 0; i -= 9)
                {
                    if (i < 9)
                    {
                        data.push_back(atoi(src.substr(0, i).c_str()));
                    }
                    else
                    {
                        data.push_back(atoi(src.substr(i - 9, 9).c_str()));
                    }
                }
                trim();
            }

            ~LongInt ()
            {
            }

            void print () const
            {
                printf("%d", data.empty() ? 0 : data.back());
                for (int i = (int) data.size() - 2; i >= 0; --i)
                {
                    printf("%09d", data[i]);
                }
            }

            LongInt & operator += (const LongInt & src)
            {
                int carry = 0;

                for (size_t i = 0; i < std::max(data.size(), src.data.size()) || carry; ++i)
                {
                    if (i == data.size())
                    {
                        data.push_back(0);
                    }
                    data[i] += carry + (i < src.data.size() ? src.data[i] : 0);
                    carry = data[i] >= base;
                    if (carry)
                    {
                        data[i] -= base;
                    }
                }
                return *this;
            }

            LongInt operator + (const LongInt & src) const
            {
                LongInt result = *this;
                return result += src;
            }

            LongInt & operator -= (const LongInt & src)
            {
                int carry = 0;
                for (size_t i = 0; i < src.data.size() || carry; ++i)
                {
                    data[i] -= carry + (i < src.data.size() ? src.data[i] : 0);
                    carry = data[i] < 0;
                    if (carry)
                    {
                        data[i] += base;
                    }
                }
                trim();
                return *this;
            }

            LongInt operator - (const LongInt & src) const
            {
                LongInt result = *this;
                return result -= src;
            }

            LongInt operator * (const LongInt & src) const
            {
                LongInt result;
                result.data.resize(data.size() + src.data.size());
                for (size_t i = 0; i < data.size(); ++i)
                {
                    for (int j = 0, carry = 0; j < (int) src.data.size() || carry; ++j)
                    {
                        long long cur = result.data[i + j]
                                + data[i] * 1ll * (j < (int) src.data.size() ? src.data[j] : 0) + carry;
                        result.data[i + j] = int(cur % base);
                        carry = int(cur / base);
                    }
                }

                result.trim();
                return result;
            }

            LongInt & operator *= (const LongInt & src)
            {
                return *this = *this * src;
            }


        private:
            void trim ()
            {
                while (data.size() > 1 && data.back() == 0)
                {
                    data.pop_back();
                }
            }
        };
    }
}



string rev(const string & src)
{
    string dst;
    for(int i=src.length()-1; i>=0; --i)
        dst.push_back(src[i]);
    return dst;
}

void generate(vector<Zeus::Numeric::LongInt> & result)
{
    // a[length][norm]
    vector<vector<vector<string> > > a;

    a.resize(MAX_LEN);
    for(int i=0; i<MAX_LEN; ++i)
    {
        a[i].resize(MAX_NORM);
    }

    a[0][0].push_back("");

    for(int length=1; length<MAX_LEN; ++length)
    {
        for(int norm=0; norm<MAX_NORM; ++norm)
        {
            for(int k=0; k<a[length-1][norm].size(); ++k)
            {
                a[length][norm].push_back(a[length-1][norm][k]);
                a[length][norm].back().push_back('0');
            }

            if(norm)
            {
                for(int k = 0; k < a[length-1][norm-1].size(); ++k)
                {
                    a[length][norm].push_back(a[length-1][norm-1][k]);
                    a[length][norm].back().push_back('1');
                }
            }
        }
    }

    for(int i=0; i<MAX_LEN; ++i)
    {
        for(int j=0; j<MAX_NORM; ++j)
        {
            for(int k=0; k<a[i][j].size(); ++k)
            {
                const string & begin = a[i][j][k];
                const string & end = rev(begin);

                if(j==0)
                {
                    result.push_back(string("2") + begin + end + "2");
                    result.push_back(string("2") + begin + "0" + end + "2");
                    result.push_back(string("2") + begin + "1" + end + "2");
                }

                if(j<2)
                {
                    result.push_back(string("1") + begin + "2" + end + "1");
                }

                result.push_back(string("1") + begin + end + "1");
                result.push_back(string("1") + begin + "0" + end + "1");
                result.push_back(string("1") + begin + "1" + end + "1");
            }
        }
    }
}

int main()
{
    vector<Zeus::Numeric::LongInt> v;
    generate(v);
    set<Zeus::Numeric::LongInt> s(v.begin(), v.end());
    s.insert(1);
    s.insert(2);
    s.insert(3);

    vector<Zeus::Numeric::LongInt> a;
    a.reserve(s.size());
    for(set<Zeus::Numeric::LongInt>::const_iterator ii = s.begin(); ii!=s.end(); ++ii)
    {
        a.push_back(*ii * (*ii));
//        a.back().print();
//        cout<<endl;
    }

    int T;
    cin>>T;

    for(int t=1; t<=T; ++t)
    {
        string s1, s2;
        cin>>s1>>s2;
        Zeus::Numeric::LongInt x(s1), y(s2);

        vector<Zeus::Numeric::LongInt>::const_iterator ii = std::lower_bound(a.begin(), a.end(), x);
        vector<Zeus::Numeric::LongInt>::const_iterator jj = std::upper_bound(a.begin(), a.end(), y);
        cout<<"Case #"<<t<<": "<<jj-ii<<endl;

    }
}
