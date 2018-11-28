#include <fstream>
#include <iostream>
#include <vector>

#define SWAP(a, b) do \
{\
    a = a + b; \
    b = a - b; \
    a = a - b; \
} while(0)

#define LOG(MSG) std::cout<<MSG<<std::endl;

int method1(const std::vector<int>& V, int& maxDiff)
{
    int cnt= 0;
    int diff = 0;
    
    for(auto i = 1; i < V.size(); ++i)
    {
//        LOG("i - 1: "<<V[i-1]);
//        LOG("i: "<<V[i]);
        diff = V[i - 1] - V[i];
        if (diff > 0)
            cnt+=diff;

        LOG("diff: "<<diff);

        if (diff > maxDiff)
            maxDiff = diff;
    }
    return cnt;
}

int method2(const std::vector<int>& V, int maxDiff)
{
    LOG("max diff: "<<maxDiff);
    int cnt= 0;
    int diff = 0;
    for(auto i = 0; i < V.size() - 1; ++i)
    {
//        LOG("i " << V[i]);
        if (V[i] < maxDiff)
            cnt+=V[i];
        else
            cnt+=maxDiff;
    }
    return cnt;
}


void testcase(int n, std::fstream &in, std::fstream &out)
{
    int N;
    std::vector<int> M;
    in>>N;
    int tmp;
    for(auto i = 1; i <= N; ++i)
    {
        in>>tmp;
        M.push_back(tmp);
    }

    int maxDiff = 0;
    int o1 = method1(M, maxDiff);
    LOG("max diff: "<<maxDiff);
    int o2 = method2(M, maxDiff);

    out<<"Case #"<<n<<": "<<o1<<" "<<o2<<std::endl;
}


int main()
{
    std::fstream in, out;
    in.open("mushroom.in", std::ios::in);
    out.open("mushroom.out", std::ios::out);
    int N;
    in>>N;
    LOG("Testcases: "<<N);
    for (auto n = 1; n <= N; ++n)
        testcase(n, in, out);

    return 0;
}
