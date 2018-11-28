#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <vector>

#define LOG(MSG) std::cout<<__LINE__<<": "<<MSG<<std::endl;
#define LOGV(b,e) do {\
    auto c = b; \
    std::ostringstream strm; \
    while(c != e) \
    { \
        strm<<*c; \
        c++; \
    } \
    LOG(strm.str()); \
} while(0)

typedef std::pair<char, bool> RES;

RES i('i', false);
RES j('j', false);
RES k('k', false);
RES one('1', false);

RES negi('i', true);
RES negj('j', true);
RES negk('k', true);
RES negone('1', true);

typedef std::map<char, RES> LMUL;

LMUL ONE {
    { '1', one },
    { 'i', i },
    { 'j', j },
    { 'k', k },
};

LMUL I {
    { '1', i },
    { 'i', negone },
    { 'j', k },
    { 'k', negj },
};

LMUL J {
    { '1', j },
    { 'i', negk },
    { 'j', negone },
    { 'k', i },
};

LMUL K {
    { '1', k },
    { 'i', j },
    { 'j', negi },
    { 'k', negone },
};

std::map<char, LMUL> TABLE {
    {'1', ONE},
    {'i', I},
    {'j', J},
    {'k', K},
};



bool testk(std::vector<char>&v, std::vector<char>::iterator it)
{
    //LOG("TESTING k");
    if(it == v.end())
    {
      //  LOG("TESTING k false");
        return false;
    }

    //LOGV(it, v.end());

    char res;
    bool sign;
    auto i = it;
    do {
        if(i == it)
        {
            res = *i;
            sign = false;
        }
        else
        {
            auto& p = TABLE[res][*i];
            sign = sign ^ p.second;
            res = p.first;
        }

        //LOG("Res: "<<res<<" sign: "<<sign);
        i++;
    } while(i != v.end());

    if (res == 'k' and sign == false)
    {
        return true;
    }

    //LOG("Res: "<<res<<" sign:"<<sign);

  //  LOG("TESTING k false");
    return false;
}

bool testj(std::vector<char>&v, std::vector<char>::iterator it)
{
    //LOG("TESTING j");

    if(it == v.end())
    {
      //  LOG("TESTING k false");
        return false;
    }

//    LOGV(it, v.end());

    char res;
    bool sign;
    auto i = it;
    do {
        if(i == it)
        {
            res = *i;
            sign = false;
        }
        else
        {
            auto& p = TABLE[res][*i];
            sign = sign ^ p.second;
            res = p.first;
        }

        if (res == 'j' and sign == false)
        {
  //          LOGV(it, i + 1);
            if(testk(v, i + 1))
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        i++;
    } while(i != v.end());

 //   LOG("TESTING j false");
    return false;
}

bool testi(std::vector<char>&v, std::vector<char>::iterator it)
{
   // LOG("Testing i");
   // LOGV(it, v.end());
    char res;
    bool sign;
    auto i = it;
    do {
        if(i == it)
        {
            res = *i;
            sign = false;
        }
        else
        {
            auto& p = TABLE[res][*i];
            sign = sign ^ p.second;
            res = p.first;
        }

        if (res == 'i' and sign == false)
        {
     //       LOGV(it, i+1);
            if(testj(v, i + 1))
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        i++;
    } while(i != v.end());

    return false;
}

void testcase(int n, std::fstream &in, std::fstream &out)
{
    std::string s;
    int chars, r;
    std::vector<char> V;
    in>>chars;
    in>>r;
    in>>s;

    for(auto i=0; i<r; ++i)
        for(auto j=0;j<chars;++j)
            V.push_back(s[j]);

    if(testi(V, V.begin()))
    {
        LOG("Case #"<<n<<": YES");
        out<<"Case #"<<n<<": YES"<<std::endl;
    }
    else
    {
        LOG("Case #"<<n<<": NO");
        out<<"Case #"<<n<<": NO"<<std::endl;
    }
}





int main()
{
    std::fstream in, out;
    in.open("dijkstra.in", std::ios::in);
    out.open("dijkstra.out", std::ios::out);
    int N;
    in>>N;
    LOG("Testcases: "<<N); 
    for (auto n = 1; n <= N; ++n)
        testcase(n, in, out);

    return 0;
}
