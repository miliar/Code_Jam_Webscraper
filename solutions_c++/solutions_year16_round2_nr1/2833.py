#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

void solve(char S[], char result[]);
int getIdx(char ch);
int main()
{
    int T;
    int cnt=1;
    scanf("%d", &T);
    while (cnt <= T)
    {
        char S[5000]={0};
        char result[5000]={0};
        scanf("%s", S);
        solve(S, result);
        printf("Case #%d: %s\n", cnt, result);
        cnt++;
    }

    return 0;
}

void solve(char S[], char result[])
{
    int ALPHA[30]={0};
    int len = strlen(S);
    vector<int> rst;
    for(int i=0; i<len ;i++)
    {
        int idx = getIdx(S[i]);
        ALPHA[idx]++;
    }
    /*
    for(int i=0; i<26; i++)
    {
        printf("%d ",ALPHA[i]);
    }
    printf("\n");
    */
    while(len > 0)
    {
        if(ALPHA[getIdx('E')]>=1 && ALPHA[getIdx('I')]>=1 && ALPHA[getIdx('G')]>=1 && ALPHA[getIdx('H')]>=1 && ALPHA[getIdx('T')]>=1)
        {
            ALPHA[getIdx('E')]--;
            ALPHA[getIdx('I')]--;
            ALPHA[getIdx('G')]--;
            ALPHA[getIdx('H')]--;
            ALPHA[getIdx('T')]--;
            rst.push_back(8);
            len -= 5;
            //printf("8\n");
        }
        else if(ALPHA[getIdx('F')]>=1 && ALPHA[getIdx('O')]>=1 && ALPHA[getIdx('U')]>=1 && ALPHA[getIdx('R')]>=1)
        {
            ALPHA[getIdx('F')]--;
            ALPHA[getIdx('O')]--;
            ALPHA[getIdx('U')]--;
            ALPHA[getIdx('R')]--;
            rst.push_back(4);
            len -= 4;
            //printf("4\n");
        }
        else if(ALPHA[getIdx('Z')]>=1 && ALPHA[getIdx('E')]>=1 && ALPHA[getIdx('R')]>=1 && ALPHA[getIdx('O')]>=1)
        {
            ALPHA[getIdx('Z')]--;
            ALPHA[getIdx('E')]--;
            ALPHA[getIdx('R')]--;
            ALPHA[getIdx('O')]--;
            rst.push_back(0);
            len -= 4;
            //printf("0\n");
        }
        else if(ALPHA[getIdx('S')]>=1 && ALPHA[getIdx('I')]>=1 && ALPHA[getIdx('X')]>=1)
        {
            ALPHA[getIdx('S')]--;
            ALPHA[getIdx('I')]--;
            ALPHA[getIdx('X')]--;
            rst.push_back(6);
            len -= 3;
            //printf("6\n");
        }
        else if(ALPHA[getIdx('T')]>=1 && ALPHA[getIdx('W')]>=1 && ALPHA[getIdx('O')]>=1)
        {
            ALPHA[getIdx('T')]--;
            ALPHA[getIdx('W')]--;
            ALPHA[getIdx('O')]--;
            rst.push_back(2);
            len -= 3;
            //printf("2\n");
        }
        else if(ALPHA[getIdx('T')]>=1 && ALPHA[getIdx('H')]>=1 && ALPHA[getIdx('R')]>=1 && ALPHA[getIdx('E')]>=2)
        {
            ALPHA[getIdx('T')]--;
            ALPHA[getIdx('H')]--;
            ALPHA[getIdx('R')]--;
            ALPHA[getIdx('E')]--;
            ALPHA[getIdx('E')]--;
            rst.push_back(3);
            len -= 5;
            //printf("3\n");
        }
        else if(ALPHA[getIdx('S')]>=1 && ALPHA[getIdx('E')]>=2 && ALPHA[getIdx('V')]>=1 && ALPHA[getIdx('N')]>=1)
        {
            ALPHA[getIdx('S')]--;
            ALPHA[getIdx('E')]--;
            ALPHA[getIdx('V')]--;
            ALPHA[getIdx('E')]--;
            ALPHA[getIdx('N')]--;
            rst.push_back(7);
            len -= 5;
            //printf("7\n");
        }
        else if(ALPHA[getIdx('O')]>=1 && ALPHA[getIdx('N')]>=1 && ALPHA[getIdx('E')]>=1)
        {
            ALPHA[getIdx('O')]--;
            ALPHA[getIdx('N')]--;
            ALPHA[getIdx('E')]--;
            rst.push_back(1);
            len -= 3;
            //printf("1\n");
        }
        else if(ALPHA[getIdx('N')]>=2 && ALPHA[getIdx('I')]>=1 && ALPHA[getIdx('E')]>=1)
        {
            ALPHA[getIdx('N')]--;
            ALPHA[getIdx('I')]--;
            ALPHA[getIdx('N')]--;
            ALPHA[getIdx('E')]--;
            rst.push_back(9);
            len -= 4;
            //printf("9\n");
        }
        else if(ALPHA[getIdx('F')]>=1 && ALPHA[getIdx('I')]>=1 && ALPHA[getIdx('V')]>=1 && ALPHA[getIdx('E')]>=1)
        {
            ALPHA[getIdx('F')]--;
            ALPHA[getIdx('I')]--;
            ALPHA[getIdx('V')]--;
            ALPHA[getIdx('E')]--;
            rst.push_back(5);
            len -= 4;
            //printf("5\n");
        }
        /*
        else
        {
            //printf("%d:%d %d:%d %d:%d %d:%d\n", getIdx('Z'), ALPHA[getIdx('Z')], getIdx('E'), ALPHA[getIdx('E')], getIdx('R'), ALPHA[getIdx('R')], getIdx('O'), ALPHA[getIdx('O')]);
            printf("%d %d %d %d\n", ALPHA[getIdx('Z')], ALPHA[getIdx('E')], ALPHA[getIdx('R')], ALPHA[getIdx('O')]);
            if(ALPHA[getIdx('Z')]>1 && ALPHA[getIdx('E')]>1 && ALPHA[getIdx('R')]>1 && ALPHA[getIdx('O')]>1)
            {
                ALPHA[getIdx('Z')]--;
                ALPHA[getIdx('E')]--;
                ALPHA[getIdx('R')]--;
                ALPHA[getIdx('O')]--;
                rst.push_back(0);
                len -= 4;
                printf("0\n");
            }
        }
        */
    }
    sort(rst.begin(), rst.end());
    for(int i=0; i<rst.size(); i++)
    {
        result[i] = (char)rst[i] + '0';
    }
}

int getIdx(char ch)
{
    return (int)ch - (int)'A';
}
