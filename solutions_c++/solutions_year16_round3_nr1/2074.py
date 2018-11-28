#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cctype>
#include<cstdio>
#include<string>
#include<cmath>

using namespace std;

#define ull unsigned long long
#define vull vector<ull>
#define ll long long
#define vll vector<ll>

struct greater
{
    template<class T>
    bool operator()(T const &a, T const &b) const { return a > b; }
};

#define SortVectorA(V) sort(V.begin(), V.end())
#define SortVectorD(V) sort(V.begin(), V.end(), ::greater())

#define PrintVector(Vector) { for(ull ii = 0 ; ii < Vector.size() ; ++ii) { cout << Vector[ii] << " "; } cout << endl; }
#define ReverseVector(V) reverse(V.begin(), V.end())
#define InsertAt(V,Position,Element) V.insert(V.begin() + Position, Element)
#define RemoveFrom(V,Position,Elements) V.erase(V.begin() + Position, V.begin() + Position + Elements)

#define BSearch(Haystack,Needle) binary_search(Haystack.begin(),Haystack.end(),Needle)
#define Find(Haystack,Needle) find(Haystack.begin(),Haystack.end(),Needle)
#define Count(Haystack,Target) count(Haystack.begin(),Haystack.end(),Target)

#define MinElementAt(V) distance(V.begin(),min_element(V.begin(),V.end()))
#define MaxElementAt(V) distance(V.begin(),max_element(V.begin(),V.end()))

#define FE() for( ; ; )
#define F0(ii, a) for( ull ii = (0) ; ii < (a); ++ii )
#define F1(ii, a) for( ull ii = (1) ; ii <= (a); ++ii )
#define Fmn(ii, m, n) for( ull ii = (m) ; ii < (n); ++ii )

#define F0r(ii, a) for( ull ii = (a) ; ii != (0); --ii )
#define F1r(ii, a) for( ull ii = (a) ; ii != (1); --ii )
#define Fmnr(ii, m, n) for( ull ii = (n) ; ii != (m); --ii )

#define Fs(ii, container) for( size_t ii = 0; ii < container.size(); ++ii )
#define Fsr(ii, container) for( size_t ii = container.size() - 1; ii != 0 ; --ii )

void GeneratePrimes(vector<ull> &Primes,ull NPrimes)
{
    Primes.clear();
    Primes.push_back(2);
    ull PrimeCount = 1;
    for( ull Candidate = 3 ; Primes.size() < NPrimes ; Candidate += 2)
    {
        bool IsPrime = true;
        for(ull ii = 0 ; Primes[ii] <= sqrt(Candidate) ; ++ii)
        {
            if(Candidate % Primes[ii] == 0)
            {
                IsPrime = false;
                break;
            }
        }
        if(IsPrime)
        {
            Primes.push_back(Candidate);
            ++PrimeCount;
        }
    }
}

bool IsOkay(vull Data)
{
    ull Sum = 0 ;
    for(ull ii = 0 ; ii < Data.size() ; ii++)
        Sum += Data[ii];
    for(ull ii = 0 ; ii < Data.size() ; ii++)
        if(Data[ii] > Sum/2)
            return false;
    return true;
}

int main()
{
    ull Tests;
    cin >> Tests;
    F1(tt,Tests)
    {
        ull Parties;
        cin>>Parties;
        vull Data;
        string Out;
        for(ull ii = 0, Temp ; ii< Parties ; ii++)
        {
            cin>>Temp;
            Data.push_back(Temp);
        }

        FE()
        {
            //PrintVector(Data);
            bool IsDone = true;
            for(ull kk = 0 ; kk<Data.size() ; kk++)
                if(Data[kk]!=0)
                    IsDone = false;
            if(IsDone) break;
            ull First = 27, Second = 27;
            for(ull kk = 0 ; kk<Data.size() ; kk++)
            {
                if(Data[kk] ==0) continue;
                //cout << "kk = " << kk << endl;
                Data[kk]--;
                for(ull mm = 0 ; mm<Data.size() ; mm++)
                {
                    if(Data[mm] ==0) continue;
                //    cout << "mm = " << mm << endl;
                    Data[mm]--;
                    if(!IsOkay(Data))
                    {
                        Data[mm]++;
                        continue;
                    }
                //    cout << "Worked 2"<< endl ;
                    Second = mm;
                    break;
                }
                if(!IsOkay(Data))
                {
                    Data[kk]++;
                    continue;
                }
            //    cout << "Worked 1"<< endl ;
                First = kk;
                if(First!=27 || Second!=27) break;
            }

            //cout << "Rsult"   << string(1,(char)(65 + First)) <<" " <<string(1,(char)(65 + Second)) << endl;

            if(First!=27) Out += " " + string(1,(char)(65 + First));
            if(Second!=27) Out += string(1,(char)(65 + Second));
        }
        cout << "Case #"<< tt << ":"<< Out << endl;
    }
    return 0;
}
