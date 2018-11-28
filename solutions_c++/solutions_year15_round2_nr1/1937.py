#include <bits/stdc++.h>
using namespace std;

struct step
{
    int num;
    int i;
};

int rev(int f)
{
    int res = 0;
    while(f)
    {
        int rem = f % 10;
        res = (res * 10) + rem;
        f /= 10;
    }
    return res;
}

int main()
{
    int tc;
    scanf("%d", &tc);
    ofstream myfile;
    myfile.open("output9.txt");
    for(int ncase = 1; ncase <= tc; ncase++)
    {
        map <int , int> exists;
        exists[1] = 1;

        int n; scanf("%d",&n);
        step s;
        s.num = 1; s.i = 1;
        queue <step> q;
        q.push(s);
        int st = 1;
        while(true)
        {
            step f = q.front();
           // printf("%d ", f.num);
            q.pop();
            if(f.num == n)
            {
                st = f.i;
                break;
            }



            s.num = f.num+1;
            s.i = f.i+1;
            if(exists[s.num] == 0)
            {
                q.push(s);
                exists[s.num] = 1;
            }

            if(f.num > 9){
              int r = rev(f.num);
              s.num = r;
              s.i = f.i + 1;

                if(exists[s.num] == 0)
                {
                    q.push(s);
                    exists[s.num] = 1;
                }
            }
        }
      //  printf("\n");
        //printf("Case #%d: %d\n", ncase, st);
        myfile << "Case #"<<ncase<<": " << st << endl;
    }
    myfile.close();
}
