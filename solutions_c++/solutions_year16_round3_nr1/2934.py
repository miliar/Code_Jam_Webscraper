#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <iterator>
#include <map>
#include <cstring>
#include <climits>
#include <time.h>

using namespace std;

#define READ() 	freopen("in.txt","r",stdin)
#define WRITE() freopen("out.txt","w",stdout)
#define sf(n) 	scanf("%d",&n)
#define lsf(n) 	scanf("%lld", &n)
#define pb(n) 	push_back(n)
#define EPS 	1e-10
#define NL 		printf("\n")
#define INF     INT_MAX
#define MAX     INT_MAX
#define MOD     1000000007
#define LL      long long

class data
{
public:
    int index;
    int val;
};

class vecSort
{
public:
    bool operator()(data const &x1, data const &x2)
    {
        if(x1.val < x2.val)return true;
        else return false;
    }

};

int n;
int arr[100];
bool isValid(int xi,int x)
{
    bool valid = false;
    arr[xi] -= x;

    if(arr[xi] < 0)
    {
        arr[xi] += x;

        return false;
    }

    int mx = -1;
    int mI;
    for(int i=0;i<n;i++)
    {
        if(arr[i] > mx)
        {
            mx = arr[i];
            mI = i;
        }

    }

    for(int i=0;i<n;i++)
    {
        if(mx == arr[i] && i!=mI)
        {
            arr[xi] += x;

//            char c = xi+65;
//            cout << "YOLO : ";
//            cout << c << endl;


            return true;
        }
    }
    arr[xi] += x;
    return false;
}

bool isValid2(int xi,int yi)
{
    arr[xi]--;arr[yi]--;
    if(arr[xi] < 0 || arr[yi] < 0)
    {
        arr[xi]++;arr[yi]++;
        return false;
    }

    int mx = -1;
    int mI;
    for(int i=0;i<n;i++)
    {
        if(arr[i] > mx)
        {
            mx = max(mx,arr[i]);
            mI = i;
        }
    }

    for(int i=0;i<n;i++)
    {
        if(mx == arr[i] && i!=mI)
        {
            arr[xi]++;arr[yi]++;
            return true;
        }
    }
    arr[xi]++;arr[yi]++;
    return false;

}




int main()
{
    READ();
    WRITE();

    int t;
    cin >> t;
    int TC = 0;

    while(t--)
    {

        cin >> n;

        vector <data> vec;

        data d1;
        for(int i=0;i<n;i++)
        {
            cin >> arr[i];
//            d1.index = i+1;
//            d1.val = arr[i];
//            vec.pb(d1);

        }


        cout << "Case #" << ++TC << ": ";

        bool done = false;
        while(!done)
        {
            done = true;
            for(int i=0;i<n;i++)
            {
                if(arr[i] > 0)
                {
                    done = false;
                    break;
                }
            }

            if(!done)
            {
                for(int i=0;i<n;i++)
                {

                    for(int j=i+1;j<n;j++)
                    {
                        if(isValid(i,1))
                        {
//                            cout << "here";
                            arr[i] -= 1;
                            char c = i+65;
                            cout << c;
//                            cout << c;
                            cout << " ";
                        }
                        else if(isValid(j,1))
                        {
                            arr[j] -= 1;
                            char c = j+65;
                            cout << c;
//                            cout << c;
                            cout << " ";
                        }
                        else if(isValid2(i,j))
                        {
                            arr[i]--;arr[j]--;
                            char c = i+65;
                            char c2 = j+65;
                            cout << c;
                            cout << c2;
                            cout << " ";
                        }
                        else if(isValid(i,2))
                        {
//                            cout << "here";
                            arr[i] -= 2;
                            char c = i+65;
                            cout << c;
                            cout << c;
                            cout << " ";
                        }
                        else if(isValid(j,2))
                        {
                            arr[j] -= 2;
                            char c = j+65;
                            cout << c;
                            cout << c;
                            cout << " ";
                        }

                    }
                }
            }

            done = true;
            for(int i=0;i<n;i++)
            {
                if(arr[i] > 0)
                {
                    done = false;

                    break;
                }
            }
        }
        cout << endl;


//        sort(vec.begin(),vec.end(),vecSort());

//        for(int i=0;i<n;i++)cout << vec[i].val << endl;

//        bool done = false;
//        while(!done)
//        {
//            done = true;
//            for(int i=0;i<n;i++)
//            {
//                if(arr[i] > 0)
//                {
//                    done = false;
//                    break;
//                }
//            }
//
//
//            if(!done)
//            {
//                sort(vec.begin(),vec.end(),vecSort());
////                cout << vec[vec.size()-1].val << endl;
//                int xMax = vec[vec.size()-1].val;
//
//                if(xMax == )
//
//
//                for(int i=vec.size()-2;i>=0;i--)
//                {
//                    if(vec[i].val + 2 == xMax) // move 2 max
//                    {
//                        char c = vec[vec.size()-1].index+64;
//                        cout << c ;
//                        cout << c ;
//                        cout << " ";
//                        arr[(vec[vec.size()-1].index)-1] -= 2;
//                        break;
//                    }
//                    else if(vec[])
//                }
//            }
//            done = true;
//        }
    }


    return 0;
}
