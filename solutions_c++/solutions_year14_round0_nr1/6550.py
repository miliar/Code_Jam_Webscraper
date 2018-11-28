#include <set>

#include <cstdio>

int
main()
{
    int case_count;
    std::scanf("%d", &case_count);

    for (int case_index = 0; case_index < case_count; case_index++) {
        std::set<int> possible_cards;

        int first_row;
        scanf("%d", &first_row);

        for (int i = 1; i < first_row; i++) {
            scanf("%*d %*d %*d %*d");
        }
        for (int i = 0; i < 4; i++) {
            int card;
            scanf("%d", &card);
            possible_cards.insert(card);
        }
        for (int i = first_row; i < 4; i++) {
            scanf("%*d %*d %*d %*d");
        }

        int second_row;
        scanf("%d", &second_row);

        // -1: Bad magician!
        // 0: Volunteer cheated!
        // >0: The card.
        int result = 0;

        for (int i = 1; i < second_row; i++) {
            scanf("%*d %*d %*d %*d");
        }
        for (int i = 0; i < 4; i++) {
            int card;
            scanf("%d", &card);
            if (possible_cards.count(card) > 0) {
                if (result == 0) {
                    result = card;
                } else {
                    result = -1;
                }
            }
        }
        for (int i = second_row; i < 4; i++) {
            scanf("%*d %*d %*d %*d");
        }

        switch (result) {
        case -1:
            printf("Case #%d: Bad magician!\n", case_index + 1);
            break;
        case 0:
            printf("Case #%d: Volunteer cheated!\n", case_index + 1);
            break;
        default:
            printf("Case #%d: %d\n", case_index + 1, result);
            break;
        }
    }

    return 0;
}
