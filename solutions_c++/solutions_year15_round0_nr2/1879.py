#include <bits/stdc++.h>

using namespace std;

void update_eat(map<int,int> &prev, map<int,int> &next, int val) {
    int parts = 1, previous = val + 1;
    int max_part = val;


    while(true) {
        auto it = prev.upper_bound(max_part);
        if( it != prev.begin() ) {
            it--;
            auto it2 = next.lower_bound(max_part);
            if( it2 == next.end() || it2->first != max_part) {
                next.insert( it2, make_pair( max_part, it->second + parts - 1 ) );
            } else if( it2->second > it->second + parts - 1 )  {
                it2->second = it->second + parts-1;
            }
            it++;
        }
        for( ; it != prev.end(); it++ ) {
            auto it2 = next.lower_bound(it->first);
            if( it2 == next.end() || it2->first != it->first ) {
                next.insert( it2, make_pair( it->first, it->second + parts - 1 ) );
            } else if( it2->second > it->second + parts - 1 )  {
                it2->second = it->second + parts-1;
            }
        }
ADD_PART:
        ++parts;
        max_part = ( val + parts - 1 ) / parts;
        if( max_part + parts - 1 >= val )
            return;
        if( max_part == previous ) 
            goto ADD_PART;
        previous = max_part;
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    int numbers[1024];
    int time_to_eat[1024][10], added_minutes[1024][10];
    map<int,int> maps[2], *ma, *mb;
    ma = &maps[0];
    mb = &maps[1];

    int T;
    cin >> T;
    for( int CASE = 1; CASE <= T; CASE++ ) {
        int D;
        cin >> D;

        for( int i = 0; i < D; i++ )
            cin >> numbers[i];

        sort(numbers,numbers+D);

        ma->clear();
        (*ma)[0] = 0;
        for( int i = 0; i < D; i++ ) {
            mb->clear();
            //cout << "Making: " << numbers[i] << endl;
            update_eat(*ma,*mb,numbers[i]);
            swap(ma,mb);
            /*for( auto it : *ma ) { 
                cout << it.first << " " << it.second << endl;
            }*/
        }
        int best = numbers[D-1];
        for( auto it : *ma ) { 
            if( it.first + it.second < best )
                best = it.first + it.second;
        }
        
        cout << "Case #" << CASE << ": " << best << endl;
    }

    return 0;
}
