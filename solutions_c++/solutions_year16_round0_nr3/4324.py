#include <bits/stdc++.h>

using namespace std;

int T, J, N, found;
string curStr;
vector <long long> answer;

long long isPrime(long long curNum)
{
    if (curNum % 2 == 0) return 2;
    for (long long i = 3; i * i <= curNum; i += 2)
    {
        //cout<<i<<endl;
            if (curNum % i == 0) return i;
    }
    return -1;
}

long long curBase(long long num, int base)
{
    long long mult = 1, answ = 0;
    while (num)
    {
        answ += mult * (num % 10);
        num /= 10;
        mult *= base;
    }
    return answ;
}

map <string, bool> used;

void check(string cur)
{
    answer.clear();
    long long num = 1;
    for (int i = 1; i < cur.size(); ++i)
    {
        num *= 10;
        if (cur[i] == '1') num +=1;
    }
    for (int base = 2; base <= 10; ++base)
    {
        long long curNum = curBase(num, base);
        long long dev = isPrime(curNum);
        if (dev != -1) answer.push_back(dev);

        else return;
    }
    found++;

    cout<<cur;
    for (int i = 0; i < answer.size(); ++i)
        printf(" %lld", answer[i]);
    printf("\n");

}

void bruteForce(int indx, char symb)
{
    if (found == J) return;
    curStr[indx] = symb;
    if (indx == 1) {check(curStr);return;}

    //if (used[curStr]) return;
    if (indx < 0) return;



    //cout<<curStr<<endl;
    bruteForce(indx - 1, '1');
   // used[curStr] = 1;
    bruteForce(indx - 1, '0');
   // used[curStr] = 1;
}

int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    scanf("%d", &T);//cout<<T<<endl;
    for (int i = 0; i < T; ++i)
    {
        printf("Case #%d:\n", i + 1);

        curStr.clear();
        found = 0;
        curStr += '1';
        scanf("%d %d", &N, &J);
        for (int j = 1; j < N - 1; ++j)
            curStr += '0';
        curStr += '1';
        bruteForce(curStr.size() - 2, '1');
    }
}
