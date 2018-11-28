#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Group {
    int count;
    bool happy;
};

void flip(vector<Group*> *data) {
    Group *c = data->at(0);
    c->happy = !c->happy;
    if(data->size() > 1) {
        Group *n = data->at(1);
        if(n->happy == c->happy) {
            n->count += c->count;
            data->erase(data->begin());
            delete c;
        }
    }
}

int solve(string map) {
    vector<Group*> data;
    Group *c;
    int count = map.size();
    Group *g = new Group();
    g->count = 1;
    g->happy = map[0] == '+';
    for (int i = 1; i < count; ++i) {
        char ch = map[i];
        bool happy = ch == '+';
        if(g->happy != happy) {
            data.push_back(g);
            g = new Group();
            g->count = 1;
            g->happy = happy;
        } else {
            g->count++;
        }
    }

    if(g->happy == false)
        data.push_back(g);

    int flipCount = 0;
    if(data.size() > 0) {
        while(true) {
            c = data.at(0);
            if (c->happy && data.size() == 1)
                break;

            flip(&data);
            flipCount++;
        }
    }

    return flipCount;
}

int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        string line;
        cin >> line;
        int result = solve(line);
        cout << "Case #" << i << ": " << result << endl;
    }
    return 0;
}