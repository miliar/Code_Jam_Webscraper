#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long number;

vector<number> v;

void init()
{
    v.reserve(200);
    v.push_back(number(0ll));
    v.push_back(number(1ll));
    v.push_back(number(4ll));
    v.push_back(number(9ll));
    v.push_back(number(121ll));
    v.push_back(number(484ll));
    v.push_back(number(10201ll));
    v.push_back(number(12321ll));
    v.push_back(number(14641ll));
    v.push_back(number(40804ll));
    v.push_back(number(44944ll));
    v.push_back(number(1002001ll));
    v.push_back(number(1234321ll));
    v.push_back(number(4008004ll));
    v.push_back(number(100020001ll));
    v.push_back(number(102030201ll));
    v.push_back(number(104060401ll));
    v.push_back(number(121242121ll));
    v.push_back(number(123454321ll));
    v.push_back(number(125686521ll));
    v.push_back(number(400080004ll));
    v.push_back(number(404090404ll));
    v.push_back(number(10000200001ll));
    v.push_back(number(10221412201ll));
    v.push_back(number(12102420121ll));
    v.push_back(number(12345654321ll));
    v.push_back(number(40000800004ll));
    v.push_back(number(1000002000001ll));
    v.push_back(number(1002003002001ll));
    v.push_back(number(1004006004001ll));
    v.push_back(number(1020304030201ll));
    v.push_back(number(1022325232201ll));
    v.push_back(number(1024348434201ll));
    v.push_back(number(1210024200121ll));
    v.push_back(number(1212225222121ll));
    v.push_back(number(1214428244121ll));
    v.push_back(number(1230127210321ll));
    v.push_back(number(1232346432321ll));
    v.push_back(number(1234567654321ll));
    v.push_back(number(4000008000004ll));
    v.push_back(number(4004009004004ll));
    v.push_back(number(100000020000001ll));
    v.push_back(number(100220141022001ll));
    v.push_back(number(102012040210201ll));
    v.push_back(number(102234363432201ll));
    v.push_back(number(121000242000121ll));
    v.push_back(number(121242363242121ll));
    v.push_back(number(123212464212321ll));
    v.push_back(number(123456787654321ll));
    v.push_back(number(400000080000004ll));
    v.push_back(number(10000000200000001ll));
    v.push_back(number(10002000300020001ll));
    v.push_back(number(10004000600040001ll));
    v.push_back(number(10020210401202001ll));
    v.push_back(number(10022212521222001ll));
    v.push_back(number(10024214841242001ll));
    v.push_back(number(10201020402010201ll));
    v.push_back(number(10203040504030201ll));
    v.push_back(number(10205060806050201ll));
    v.push_back(number(10221432623412201ll));
    v.push_back(number(10223454745432201ll));
    v.push_back(number(12100002420000121ll));
    v.push_back(number(12102202520220121ll));
    v.push_back(number(12104402820440121ll));
    v.push_back(number(12122232623222121ll));
    v.push_back(number(12124434743442121ll));
    v.push_back(number(12321024642012321ll));
    v.push_back(number(12323244744232321ll));
    v.push_back(number(12343456865434321ll));
    v.push_back(number(12345678987654321ll));
    v.push_back(number(40000000800000004ll));
    v.push_back(number(40004000900040004ll));
    v.push_back(number(1000000002000000001ll));
}

int main()
{
    freopen("c.txt", "r", stdin);
    freopen("c-out.txt", "w", stdout);

    init();
    int T;
    number a, b;
    cin >> T;
    for (int cs = 1; cs <= T; ++cs)
    {
        cin >> a >> b;
        vector<number>::iterator l, u;
        l = lower_bound(v.begin(), v.end(), a);
        u = upper_bound(v.begin(), v.end(), b);
        int z = u - l;
        cout << "Case #" << cs << ": " << z << endl;
    }
    return 0;
}
