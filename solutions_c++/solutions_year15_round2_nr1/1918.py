#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <string.h>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#define inf (long long)1e15
#define MAX_N 20

using namespace std;

long long int rev(long long int n)
{
    if(n == 0)return 0;
    long long int k = 0;
    while(n!=0)
    {
        k = 10*k + (n%10);
        n = n/10;
    }
    return k;
}
///standard bfs
int main()
{
   ifstream in("input.txt");
   ofstream out("output.txt");
   long long int test_case;
   cin >> test_case;
   for(long long int i = 0; i < test_case; i++)
   {
       long long int n;
       cin >> n;
       vector <bool> seen(91000100, 0);
       vector <long long int> dist(91000100, 0);
       queue <long long int> q;
       q.push(1);
       seen[1] = 1;
       dist[1] = 1;
       bool flag = 0;
       while(q.size()!=0)
       {
           long long int t = q.front();
           q.pop();
           long long int right_node = t + 1;
           long long int left_node = rev(t);
           if(!seen[right_node])
           {
               q.push(right_node);
               seen[right_node] = 1;
               dist[right_node] = dist[t] + 1;
           }
           if(!seen[left_node])
           {
               q.push(left_node);
               seen[left_node] = 1;
               dist[left_node] = dist[t] + 1;
           }
           if(seen[n])
           {
               break;
           }
       }
       out << "Case #" << i + 1 << ": " << dist[n] << endl;
   }
}
