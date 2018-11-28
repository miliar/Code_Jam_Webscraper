#include <fstream>
#include <iostream>
#include <vector>

#define LOG(MSG) std::cout<<MSG<<std::endl;

void testcase(int n, std::fstream &in, std::fstream &out)
{

    std::vector<int> S;
    int s;
    in>>s;
    LOG("Max shyness: "<<s);
    std::string sstr;
    in>>sstr;
    LOG(sstr);
    for(auto i = 0; i <= s; ++i)
    {
        char c = sstr[i];
        S.push_back(c - 48);
    }

    int cur = S[0];
    int friends = 0;
    for(auto i = 1; i <= s; ++i)
    {
        int curFriends = i - cur;
        if(curFriends < 0)
            curFriends = 0;
        friends += curFriends;
        cur += curFriends + S[i];
        LOG("CurFriends: "<<curFriends<<" Friends: "<< friends <<" Cur: "<<cur);
    }
    
    out<<"Case #"<<n<<": "<<friends<<std::endl;
}

int main()
{
    std::fstream in, out;
    in.open("standing.in", std::ios::in);
    out.open("standing.out", std::ios::out);
    int N;
    in>>N;
    LOG("Testcases: "<<N); 
    for (auto n = 1; n <= N; ++n)
        testcase(n, in, out);



    return 0;
}
