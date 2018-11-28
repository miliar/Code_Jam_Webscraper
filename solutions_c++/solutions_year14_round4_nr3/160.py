#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<cstdlib>
#include<cstdio>
using namespace std;

int n,x,h,k;
int heat[10020],coor[10020],t[10020],d[200020];
vector<int> scene;
int r1[10020],r2[10020],r3[10020];

int lowbit(int x)
{
    return x&(-x);
}

void update(int x,int num)
{
    while (x<=100010)
    {
        d[x] += num;
        x+=lowbit(x);
    }
}

int getSum(int x)
{
    int s = 0;
    while (x > 0)
    {
        s += d[x];
        x -= lowbit(x);
    }
    return s;
}

int main()
{
    int tt;
    scanf("%d",&tt);
    for (int ii = 0; ii < tt; ii++)
    {
        memset(d,0,sizeof(d));
        memset(r1,0,sizeof(r1));
        memset(r2,-1,sizeof(r2));
        memset(r3,-1,sizeof(r3));
        scene.clear();
        scanf("%d",&n);
        for (int i = 0; i < n; i++)
        {
            scanf("%d %d",&x,&h);
            heat[ i ] = h;
            coor[ i ] = x;
            if (h == 0) t[ i ] = 0;
            else
            {
                t[ i ] = 1;
                scene.push_back(i);
            }
        }
        int last = -1;
        for (int i = 0; i < n; i++)
        {
            if (t[ i ] == 0)
            {
                if (last == scene.size() - 1)
                {
                    r1[scene[last]]++;
                    heat[ i ] = heat[ scene[last] ];
                    continue;
                }
                if (last == -1)
                {
                    r1[scene[last + 1]]++;
                    heat[ i ] = heat[ scene[last + 1] ];
                    continue;
                }
                if (abs(coor[scene[last]] - coor[i]) > abs(coor[scene[last + 1]] - coor[i]))
                {
                    r1[scene[last + 1]]++;
                    heat[ i ] = heat[ scene[last + 1] ];
                }
                if (abs(coor[scene[last]] - coor[i]) < abs(coor[scene[last + 1]] - coor[i]))
                {
                    r1[scene[last]]++;
                    heat[ i ] = heat[ scene[last] ];
                }
                if (abs(coor[scene[last]] - coor[i]) == abs(coor[scene[last + 1]] - coor[i]))
                {
                    r2[scene[last]] = scene[last + 1];
                    r3[scene[last + 1]] = scene[last];
                    heat[ i ] = max(heat[scene[last + 1]],heat[ scene[last] ]);
                }
            }
            else last++;
        }
        for (int i = 0; i < n; i++)
            update(heat[ i ], 1);
        scanf("%d\n",&k);
        printf("Case #%d:\n",ii + 1);
        for (; k > 0; k--)
        {
            char op;
            int R,l,v;
            scanf("%s",&op);
            if (op == 'Q')
            {
                scanf("%d",&R);
                printf("%d\n",getSum(R));
            }
            else
            {
                scanf("%d %d",&l,&v);
                update(heat[ l ] , - (1 + r1[ l ]));
                if (r2[l] >= 0 )
                {
                    if (heat[ l ] > heat[r2[l]])
                        update(heat[ l ], -1);
                    else 
                        update(heat[ r2[l] ],-1);
                    if (v > heat[ r2[ l ] ])
                        update(v,1);
                    else update(heat[ r2[l] ], 1);
                }
                if (r3[l] >= 0 )
                {
                    if (heat[ l ] > heat[ r3[l] ])
                        update(heat[ l ], -1);
                    else 
                        update(heat[ r3[l] ], -1);
                    if (v > heat[ r3[ l ] ])
                        update (v,1);
                    else update(heat[ r3[l] ],1);
                }
                heat[ l ] = v;
                update(v , 1 + r1[ l ]);
            }
        }
    }
    return 0;
}
