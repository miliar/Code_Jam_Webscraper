#include<iostream>
#include<string>
#include<sstream>
#include<cmath>

using namespace std; 

bool is_fair(long long  n)
{
    stringstream ss ; 
    ss << n ; 
    string s = ss.str();
    //cout << s << endl; 
    int left = 0 ; 
    int right = s.size() - 1;
    while(left <= right)
    {
        if(s[left] != s[right] )
            return false; 
        left ++ ; 
        right -- ; 
    }    

    return true; 
}

bool is_square(long long n)
{
    long long root = (long long)sqrt(n);
    if( root * root == n && is_fair(root))
        return true; 
    else 
        return false;  
}

void work()
{
    int T ; 
    cin >> T; 
    for(int t = 1 ; t <= T ; t++)
    {
        long long a , b; 
        cin >> a >> b; 
        int count = 0 ; 
        while( a <= b) 
        {
           if(is_fair(a) && is_square(a))
                count ++  ;
          
            a++; 
        }

        cout << "Case #" << t << ": " << count << endl;
    }

}

int main()
{
    //cout << is_fair(4) <<endl; 
    //cout << is_fair(5) <<endl; 
    //cout << is_fair(6) <<endl; 
    work();
    return 0 ; 
}
