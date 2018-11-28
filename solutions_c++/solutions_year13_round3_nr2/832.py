#include<iostream>
#include<set>
#include<queue>
#include<string>
using namespace std;
    
static const int dx[] = { 1, 0, -1, 0};
static const int dy[] = { 0, 1, 0, -1};
static const char dir[] = { 'W', 'S', 'E', 'N'};

#define dbg(x) cerr << #x << " = " << x << " "

class Wave
{
private:

    struct Point
    {
        int x,y,s;
        Point( int x, int y, int s): x(x), y(y), s(s) {};
        inline bool operator< (const Point& P) const
        {
            if ( x != P.x) return x < P.x;
            if ( y != P.y) return y < P.y;
            return s < P.s;
        }
    };


public: 
    Wave( ) {};

    string find(int X, int Y)
    {
        queue<Point> QP;
        set<Point> SP;
        QP.push(Point(0,0,0));
        SP.insert(Point(0,0,0));
        bool found = false;
        int fstep = 0;
        while( !found)
        {
            Point cur = QP.front();
        //    dbg(cur.x); dbg(cur.y); dbg(cur.s) << endl;
            int step= cur.s+1;
            QP.pop();

            for (int i=0;i<4;++i)
            {
                int new_x = cur.x+step*dx[i];
                int new_y = cur.y+step*dy[i];

                if ( SP.count(Point(new_x, new_y, step))==0)
                {
                    SP.insert( Point(new_x, new_y, step));
                    QP.push( Point(new_x,new_y, step));
                }
    
                if ( new_x == X && new_y == Y)
                {
                    found = true;
                    fstep = step;
                }
            } 
        }

        string res = "";
        int curx=X, cury=Y;
        while ( fstep >0)
        {
//            dbg(curx); dbg(cury); dbg(fstep) << endl;
            for ( int i=0;i<4;++i)
            {
                int newx = curx+dx[i]*fstep;
                int newy = cury+dy[i]*fstep;
                if ( SP.count( Point( newx, newy, fstep-1)) >0)
                {
                    curx = newx;
                    cury = newy;
                    fstep--;
                    res = dir[i] + res;
                    break;
                }
            }
        }
        return res;
    }
        

};

void print( int t, string str)
{
    cout << "Case #" << t << ": " << str << endl;
}

int main()
{
    int T;
    cin >> T;
    for (int t=0;t<T;t++)
    {
        int X, Y;
        cin >> X >> Y;
        Wave W;
        print( t+1, W.find(X,Y));
    }
    return 0;
}
