#include <unordered_map>
#include <vector>

#include <thread>
#include <string>
#include <memory>

#include <iostream>
#include <future>
#include <cstdlib>
#include <algorithm>
#include <utility>
#include <functional>
#include <chrono>
#include <mutex>

using namespace std;

int main() {
    int num_inputs;
    cin >> num_inputs;

    vector<pair<int, string>> inputs;
    inputs.reserve(num_inputs);

    for (unsigned i = 0; i < num_inputs; i++) {
        int max_shyness;
        string shyrating;

        cin >> max_shyness >> shyrating;
        inputs.emplace_back(make_pair(max_shyness, shyrating));
    }

    for (unsigned j = 0; j < inputs.size(); j++) {
        int number_needed{0};
        auto maximum_shyness = inputs[j].first;
        auto str = inputs[j].second;
        int number_standing{0};
        for (unsigned i = 0; i < str.length(); i++) {
            if (str[i] != '0') {
                // there are some people with this shyness level
                if (number_standing >= i) {
                    number_standing += str[i] - '0';
                } else {
                    int number_to_trigger_ovation = (i - number_standing);
                    number_needed += number_to_trigger_ovation;

                    number_standing += number_to_trigger_ovation;
                    number_standing += str[i] - '0';
                }
            }
        }
        cout << "Case #" << j + 1 << ": " << number_needed << endl;
    }
}