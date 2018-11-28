#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int main() {
    int T, firstAnswer, secondAnswer, tmp[4], hit;
    std::string answer;

    std::cin >> T;
    for (int i=0; i < T; ++i) {
        std::vector<int> candidates;
        hit = 0;
        std::cin >> firstAnswer;
        for (int j=0; j < 4; ++j) {
            std::cin >> tmp[0] >> tmp[1] >> tmp[2] >> tmp[3];

            if (firstAnswer == j+1) {
                candidates.push_back(tmp[0]);
                candidates.push_back(tmp[1]);
                candidates.push_back(tmp[2]);
                candidates.push_back(tmp[3]);
            }
        }

        std::cin >> secondAnswer;
        for (int j=0; j < 4; ++j) {
            std::cin >> tmp[0] >> tmp[1] >> tmp[2] >> tmp[3];

            if (secondAnswer == j+1) {
                for (int k=0; k < 4; ++k) {
                    std::vector<int>::iterator it = std::find(candidates.begin(), candidates.end(), tmp[k]);
                    if (it != candidates.end()) {
                        ++hit;
                        answer = std::to_string(tmp[k]);
                    }
                }
            }
        }

        if (hit == 0) {
            answer = "Volunteer cheated!";
        } else if (hit > 1) {
            answer = "Bad magician!";
        }

        std::cout << "Case #" << i+1 << ": " << answer << std::endl;
    }

    return 0;
}
