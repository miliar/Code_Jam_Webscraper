#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Sequence
{
public:
    Sequence(int N) : N(N)
    {
        for(int i=0; i<N; i++)
        {
            vals.push_back(0);
            A.push_back(1);
            B.push_back(1);
        }

        next = 1;
    }

    int Aval(int idx)
    {
        int Amax = 0;
        for(int i=0; i<idx; i++)
        {
            if(vals[i] != 0)
                Amax = max(Amax, A[i]);
        }
        return Amax+1;
    }

    int Bval(int idx)
    {
        int Bmax = 0;
        for(int i=idx+1; i<N; i++)
        {
            if(vals[i] != 0)
                Bmax = max(Bmax, B[i]);
        }
        return Bmax+1;
    }

    bool canSet(int idx, const vector<int> &Ag, const vector<int> &Bg)
    {
        if(vals[idx] != 0)
            return false;

        return A[idx] == Ag[idx] && B[idx] == Bg[idx];
    }

    void set(int idx)
    {
        vals[idx] = next++;
        for(int i=0; i<idx; i++)
        {
            if(vals[i] == 0)
                B[i] = Bval(i);
        }
        for(int i=idx+1; i<N; i++)
        {
            if(vals[i] == 0)
                A[i] = Aval(i);
        }
    }

    bool operator<(const Sequence &other) const
    {
        for(int i=0; i<N; i++)
        {
            if(vals[i] < other.vals[i])
                return true;
            else if(vals[i] > other.vals[i])
                return false;
        }
        return false;
    }

    vector<int> vals;
    vector<int> A;
    vector<int> B;
    int N;
    int next;
};

void doCase()
{
    int N;
    cin >> N;
    vector<int> A, B;
    for(int i=0; i<N; i++)
    {
        int At;
        cin >> At;
        A.push_back(At);
    }
    for(int i=0; i<N; i++)
    {
        int Bt;
        cin >> Bt;
        B.push_back(Bt);
    }

    vector<Sequence> sequences;
    sequences.push_back(Sequence(N));
    vector<Sequence> newsequences;
    for(int digit=1; digit<=N; digit++)
    {
        for(int i=0; i<sequences.size(); i++)
        {
            for(int j=0; j<N; j++)
            {
                if(A[j] + B[j] <= digit+1)
                {
                    if(sequences[i].canSet(j, A, B))
                    {
                        Sequence newseq = sequences[i];
                        newseq.set(j);
                        newsequences.push_back(newseq);
                    }
                }
            }
        }
        sequences = newsequences;
        newsequences.clear();
    }

    sort(sequences.begin(), sequences.end());
    for(int i=0; i<N; i++)
    {
        cout << sequences[0].vals[i];
        if(i == N-1)
            cout << endl;
        else
            cout << " ";
    }

}

int main()
{
    int cases;
    cin >> cases;
    for(int i=0; i<cases; i++)
    {
        cout << "Case #" << i+1 << ": ";
        doCase();
    }
}

