#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <string>
#include <cmath>

#define CHECK_STREAM(S, E) do { \
    if (!(S)) goto E; \
} while (0)

#define CHECK_END_STREAM(S, E) do { \
    (S).ignore(2); \
    if (!(S).eof()) goto E; \
} while (0)

#define CHECK_OPEN_STREAM(S, E) do { \
    if (!(S).is_open()) goto E; \
} while (0)

auto main(int argc, char* argv[])
    -> int
{
    if (argc < 3) {
        std::cerr << "expected \'./programe filename\' n_threads ";
        return -1;
    }
    size_t N;
    std::vector<std::array<size_t, 3>> data;
    std::vector<std::vector<size_t>> res;

    std::ifstream file;
    file.open(argv[1]);
    CHECK_OPEN_STREAM(file, PARSE_ERROR);
    CHECK_STREAM(file >> N, PARSE_ERROR);
    data.resize(N);
    res.resize(N);
    for (size_t i = 0; i < N; ++i) {
        CHECK_STREAM(file >> data[i][0], PARSE_ERROR);
        CHECK_STREAM(file >> data[i][1], PARSE_ERROR);
        CHECK_STREAM(file >> data[i][2], PARSE_ERROR);
    }
    CHECK_END_STREAM(file, PARSE_ERROR);

    for (size_t i = 0; i < N; ++i) {
        size_t K = data[i][0];
        size_t C = data[i][1];
        size_t S = data[i][2];

        if ((C == 1) || (S == K)) {
            res[i].resize(K);
            for (size_t j = 0; j < res.size(); ++j) {
                res[i][j] = j + 1;
            }
        }
        else {
            size_t center = C / 2 + 1;
            size_t K_acc = K;
            while (center <= static_cast<size_t>(std::pow(K, C) / 2 + (K % 2) * K / 2.)) {
                res[i].push_back(center);
                K_acc += 1;
                center += K_acc;
            }
        }
        std::cout << "Case #" + std::to_string(i + 1) << ": ";
        if (res[i].size() > data[i][2]) {
            std::cout << "IMPOSSIBLE" << std::endl;
        }
        else {
            for (size_t j = 0; j < res[i].size(); ++j) {
                std::cout << res[i][j] << ' ';
            }
            std::cout << std::endl;
        }
    }

    return 0;
PARSE_ERROR:
    std::cerr << "error while parsing file" << std::endl;
    return -2;
}
