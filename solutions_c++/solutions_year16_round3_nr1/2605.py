#include <bits/stdc++.h>

using namespace std;

#define INF 0x7fffffff
#define forstl(i,n) for(__typeof(n.begin())i = n.begin();i!=n.end();i++)
#define rforstl(i,n) for(__typeof(n.rbegin()) i = n.rbegin(); i!= n.rend(); i++)


typedef pair<int,int> ii;
typedef pair<int, ii> iii;
typedef priority_queue<ii> pqii;
typedef priority_queue<iii> pqiii;
typedef set<int> si;
typedef map<string, int> msi;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef unsigned long ull;
typedef long long ll;


int main()
{
    //code jam
    int t;
    int cases =1;
    while(scanf("%d", &t)!=EOF)
    {
        while(t--)
        {
            printf("Case #%d: ", cases++);
            int n;
            scanf("%d", &n);
            int total =0 ;
            vector<int> numbers;
            numbers.clear();
            while(n--)
            {


                int x;
                scanf("%d", &x);
                total+=x;
                numbers.push_back(x);
            }


            while(total>0)
            {
                int hi = -INF;
                int index = -1;
                for(int i=0; i<numbers.size(); i++)
                {
                    if(hi<numbers[i])
                    {
                        hi = numbers[i];
                        index = i;
                    }
                }

                int hi2 = -INF;
                int index2 = -1;
                for(int i=0; i<numbers.size(); i++)
                {
                    if(hi2<numbers[i] && i != index)
                    {
                        hi2 = numbers[i];
                        index2 = i;
                    }
                }



                if(hi > 1)
                {
                    printf("%c", 'A'+index);
                    numbers[index]--;
                    total--;
                    bool ok = true;
                    for(int i=0; i<numbers.size(); i++)
                    {
                        if(i!=index)
                        {
                            if((numbers[i]/(total-1.00))>0.5)
                            {
                                ok = false; break;
                            }
                        }
                    }
                    if(ok)
                    {
                        printf("%c", 'A'+index);
                        total--;
                        numbers[index]--;
                    }
                    else
                    {
                        ok = true;
                        for(int i=0; i<numbers.size(); i++)
                        {
                            if(i!=index2)
                            {
                                if((numbers[i]/(total-1.00))>0.5)
                                {
                                    ok = false; break;
                                }
                            }
                        }
                        if(ok)
                        {
                            printf("%c", 'A'+index2);
                            total--;
                            numbers[index2]--;
                        }
                    }

                    if(total)
                        printf(" ");


                }
                else
                {
                    assert(total >= 2) ;
                    for(int i=0; i<numbers.size(); i++)
                    {
                        if(total == 2)
                            break;
                        if(numbers[i])
                        {
                            numbers[i]--;
                            total--;
                            printf("%c ", 'A'+i);
                        }
                    }

                    for(int i=0; i<numbers.size(); i++)
                    {
                        if(numbers[i])
                        {
                            numbers[i]--;
                            total--;
                            printf("%c", 'A'+i);
                        }
                    }
                }

                if(!total) printf("\n");



                /*if(total > 2)
                {
                    numbers[index]--;
                    total--;
                    printf("%c ", 'A'+index);
                }
                else
                {
                    for(int i=0; i<numbers.size(); i++)
                    {
                        if(numbers[i])
                            printf("%c", 'A'+i);
                    }
                    printf("\n");
                    total =0;
                }*/
            }

        }
    }
    return 0;
}


