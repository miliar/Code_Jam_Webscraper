#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

struct Mote
{
        unsigned int _s;
        unsigned int _nbCreation;
        Mote (unsigned int i):_nbCreation(0)
        {
            _s = i;
        }
        Mote():_nbCreation(0){}

        bool operator<(const Mote&m) const
        {
            return _s < m._s;
        }
};


int main() {
    unsigned int pb_size;
    cin >> pb_size;


    for (unsigned int pb_idx = 1;pb_idx <= pb_size;++pb_idx)
    {
        cerr << "Case #" << pb_idx << endl;
        unsigned int own_s = 0, n_size =0;
        cin >> own_s >> n_size;

        
        vector<Mote> other_motes;

        for (unsigned int i= 0; i < n_size;++i)
        {
            unsigned int m;
            cin >> m;
            other_motes.push_back(Mote(m));
        }

        if(own_s == 1)
        {
            cout << "Case #" << pb_idx <<": " << n_size << endl;
            continue;
        }

        sort(other_motes.begin(),other_motes.end());
        
        int nbCreation = 0;

        int i=0;
        for (; i < n_size;++i)
        {
            auto &m= other_motes[i];
            unsigned int tmp_nbCreation=0;
            while(m._s >= own_s)
            {
                tmp_nbCreation +=1;
                m._nbCreation +=1;
                own_s+=own_s;
                own_s-=1;
            }
            own_s += m._s;
            nbCreation += tmp_nbCreation;

        }
        i--;

        unsigned int cummuledCreations = 0;
        unsigned int iOffset = 0;
        unsigned int elem_count=0;
        for (;i >= 0;--i)
        {
            elem_count +=1;
            auto &m = other_motes[i];
            cummuledCreations += m._nbCreation;
            if(cummuledCreations > elem_count)
            {
                nbCreation -= (cummuledCreations - elem_count);
                elem_count=0;
                cummuledCreations = 0;
            }
        }

        cout << "Case #" << pb_idx <<": " << nbCreation << endl;

    }
}
